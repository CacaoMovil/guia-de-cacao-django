# -*- coding: utf-8 -*-
import os
import shutil

from fabric.tasks import execute

from django.core.files import File
from django.conf import settings

from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required

from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext

from django.views.generic import ListView, DetailView
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import GuidesSerializer, DownloadSerializer

from phantom_pdf import render_to_pdf

from .models import Guide, Content, Section, Download
from .exporter import render_guide


class GuideList(ListView):

    """
    This Class list all Guides objects
    from the Guide model
    """
    model = Guide
    context_object_name = 'guias'
    template_name = 'index.html'


class GuideDetail(DetailView):

    """
    This Class list one Guide object
    from the Guide model
    """
    model = Guide
    context_object_name = 'guia'
    slug_field = 'number'
    slug_url_kwarg = 'number'

    def get_context_data(self, **kwargs):
        context = super(GuideDetail, self).get_context_data(**kwargs)
        context['contenido_list'] = Content.objects.filter(
            section__guide=self.object)
        context['seccion_list'] = Section.objects.filter(
            guide=self.object).order_by('peso')
        return context


class ContentDetail(DetailView):

    """
    This class list one Content object
    from the Content model
    """
    model = Content
    context_object_name = "contenido"
    template_name = 'cacao/contenido_detail.html'

    def get_queryset(self, **kwargs):
        qs = super(ContentDetail, self).get_queryset().filter(
            section__guide=self.kwargs.get('guide'))
        return qs

    def get_context_data(self, **kwargs):
        context = super(ContentDetail, self).get_context_data(**kwargs)
        context['seccion_list'] = Section.objects.filter(
            guide=self.object.guide).order_by('peso')
        return context


@staff_member_required
def render_element(request):
    """
    This method create the render from the
    dynamic pages, creating a html file
    """
    template = 'admin/render_static.html'
    guia = Guide.objects.all()
    context = {
        'guias': guia,
    }
    if request.method == 'POST':
        download = Download()

        element_number = request.POST.get('element')

        guide_element = Guide.objects.get(number=element_number)

        download.guide = guide_element
        download.num_version = download.get_last_version(guide_element.number)
        download.save()
        try:
            execute(render_guide, element_number, download.num_version)

            file_path = os.path.join(
                settings.PERSEUS_BUILD_DIR, 'guia-%s.zip' % element_number)

            with open(file_path, 'rb') as download_file:
                download.file.save('guia%s-version%s.zip' % (element_number, download.num_version),
                                File(download_file), save=True)
                #media_file = open('nomedia.txt', 'w+')
                #media_file.close()
        except:
            download.delete()
            raise

        download.save()
        message_text = 'Se ha renderizado correctamente la guia: %s.' % guide_element.name
        messages.add_message(request, messages.INFO, message_text)

        shutil.rmtree(settings.PERSEUS_SOURCE_DIR)
        shutil.rmtree(settings.PERSEUS_BUILD_DIR)

    return render_to_response(template, context,
                              context_instance=RequestContext(request))


def create_pdf(request, guide_number):
    """
    this method convert the guide and his contents
    to PDF file based in a new template
    """
    template = 'pdf/guia_pdf.html'
    guide_obj = Guide.objects.get(number=guide_number)
    content_obj = Content.objects.filter(section__guide=guide_obj)

    context = {
        'guide_obj': guide_obj,
        'content_obj': content_obj,
    }

    if request.GET.get('print'):
        pdf_name = 'guia-%s' % guide_number
        return render_to_pdf(request, pdf_name)
    else:
        return render_to_response(template, context,
                                  context_instance=RequestContext(request))


@api_view(['GET'])
def guides_collection(request):
    """
    This method is for the api and list all guides
    with the last version
    """
    if request.method == 'GET':
        guides = Guide.objects.all()
        serializer = GuidesSerializer(guides, many=True)
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def guide_elements(request, number):
    """
    This method is for the api and return all
    the elements from a Guide in specific
    """
    try:
        download = Download.objects.filter(guide=number).all()
    except Download.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = DownloadSerializer(download, many=True)
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def guide_element(request, number, num_version):
    """
    This method is for the api and retun one specific
    element from the Guide based in her num_version
    """
    try:
        download = Download.objects.get(guide=number, num_version=num_version)
    except Download.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = DownloadSerializer(download)
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def guide_last(request, number):
    """
    This method is for the api and return the last
    version from a Guide in specific
    """
    try:
        download = Download.objects.filter(
            guide=number).order_by('-num_version')[0]
    except Download.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = DownloadSerializer(download)
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def download_guide(request, guide_id, version):
    download = get_object_or_404(Download, guide__id=guide_id, num_version=version)
    return redirect(download.file.url)
