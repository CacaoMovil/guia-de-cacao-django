"""
Utils based in Django Perseus, with minimal
changes, this accept an id from the object that 
you need render.
"""
# -*- coding: utf-8 -*-
from django_perseus.utils import find_renderers

def run_renderers(number=None):
    for render_cls in find_renderers():
        r = render_cls(number)
        r.generate()