# -*- coding: utf-8 -*-
import os
import shutil
import subprocess

from django.core.files import File
from django.conf import settings

from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required

from django.shortcuts import render_to_response
from django.template import RequestContext

from django.views.generic import ListView, DetailView
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import GuidesSerializer, GuideSerializer

from phantom_pdf import render_to_pdf

from tasks import makeRender, test_celery

from .models import Guide, Content, Section, Download

class GuideList(ListView):
    model = Guide
    context_object_name = 'guias'
    template_name = 'index.html'

class GuideDetail(DetailView):
    model = Guide
    context_object_name = 'guia'

    def get_context_data(self, **kwargs):
        context = super(GuideDetail, self).get_context_data(**kwargs)
        context['contenido_list'] = Content.objects.filter(section__guide=self.object)
        context['seccion_list'] = Section.objects.filter(guide=self.object)
        return context

class ContentDetail(DetailView):
    model = Content
    context_object_name = "contenido"
    template_name = 'cacao/contenido_detail.html'

    def get_queryset(self, **kwargs):
        qs = super(ContentDetail, self).get_queryset().filter(section__guide=self.kwargs.get('guide'))
        return qs 

    def get_context_data(self, **kwargs):
        context = super(ContentDetail, self).get_context_data(**kwargs)
        context['seccion_list'] = Section.objects.filter(guide=self.object.guide)
        return context

@staff_member_required
def renderElement(request):
    template = 'admin/render_static.html' 
    guia = Guide.objects.all()
    context = {
        'guias': guia,
    }
    if request.method == 'POST':
        download = Download()

        element_number = request.POST.get('element')

        guide_element = Guide.objects.get(number=element_number)
        
        subprocess.call(['python', 'manage.py', 'render_guia', 
            '--settings=config.export', 
            '--element=%s' %element_number,
            '--archive',
            '--filename=guia%s.zip' %element_number ])
        
        file_path = os.path.join(settings.PERSEUS_BUILD_DIR, 'guia%s.zip' %element_number)
        
        download.guide = guide_element
        download.num_version = download.get_last_version(guide_element.number)
        with open(file_path, 'rb') as download_file:
            download.file.save('guia%s-version%s.zip' %(element_number, download.get_last_version(guide_element.number)),
                                File(download_file), save=True)        
        download.save()
        
        messages.add_message(request, messages.INFO, 'Se ha renderizado correctamente.')

        shutil.rmtree(settings.PERSEUS_SOURCE_DIR)
        shutil.rmtree(settings.PERSEUS_BUILD_DIR)

    return render_to_response(template, context,
                              context_instance=RequestContext(request))
def createPdf(request):
    template = 'pdf/guia_pdf.html' 
    obj = Guide.objects.get(number=1)
    context = {
        'obj': obj,
    }
    
    if request.GET.get('print'):
        pdf_name = 'guia'
        return render_to_pdf(request, pdf_name)
    else:
        return render_to_response(template, context,
                              context_instance=RequestContext(request))
    
    return render_to_response(template, context,
                              context_instance=RequestContext(request))
        
    

@api_view(['GET'])
def guides_collection(request):
    if request.method == 'GET':
        guides = Guide.objects.all()
        serializer = GuidesSerializer(guides, many=True)
        return Response(serializer.data)
    else: 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def guide_elements(request, pk):
    try:
        download = Download.objects.filter(guide=pk).all()
    except Download.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = GuideSerializer(download, many=True)
        return Response(serializer.data)
    else: 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def guide_element(request, pk, num_version):
    try:
        download = Download.objects.get(guide=pk, num_version=num_version)
    except Download.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = GuideSerializer(download)
        return Response(serializer.data)
    else: 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def guide_last(request, pk):
    try:
        download = Download.objects.filter(guide=pk).order_by('-num_version')[0]
    except Download.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = GuideSerializer(download)
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
