# -*- coding: utf-8 -*-
from django.shortcuts import redirect

from django.views.generic import ListView, DetailView
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import GuidesSerializer, GuideSerializer

from tasks import createLink, makeRender

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

def staticGenerator(request):
    makeRender.delay('python manage.py render --settings=config.export')
    createLink.delay('./symlink.sh')
    return redirect('/admin/')

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

