# -*- coding: utf-8 -*-
from django.views.generic import ListView, DetailView
from .models import Guia, Contenido, Seccion

class GuiaList(ListView):
    model = Guia
    context_object_name = "guias"
    template_name = "index.html"

class GuiaDetail(DetailView):
    model = Guia
    context_object_name = "guia"

    def get_context_data(self, **kwargs):
        context = super(GuiaDetail, self).get_context_data(**kwargs)
        context['contenido_list'] = Contenido.objects.filter(seccion__guia=self.object)
        context['seccion_list'] = Seccion.objects.filter(guia=self.object)
        return context

class ContenidoDetail(DetailView):
    model = Contenido
    context_object_name = "contenido"

    def get_context_data(self, **kwargs):
        context = super(ContenidoDetail, self).get_context_data(**kwargs)
        context['seccion_list'] = Seccion.objects.filter(guia=self.object.guia)
        return context