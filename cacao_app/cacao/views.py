# -*- coding: utf-8 -*-
from django.views.generic import ListView, DetailView
from .models import Guide, Content, Section

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

    def get_context_data(self, **kwargs):
        context = super(ContentDetail, self).get_context_data(**kwargs)
        context['seccion_list'] = Section.objects.filter(guide=self.object.guide)
        return context