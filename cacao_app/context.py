# -*- coding: utf-8 -*-
from cacao.models import Guide

def guia_items(request):
    guide = Guide.objects.all().order_by('number')
    dicc = {
             'guide_items': guide,
           }
    return dicc