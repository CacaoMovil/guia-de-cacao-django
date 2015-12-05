"""
Utils based in Django Perseus, with minimal
changes, this accept a number from the object that
you need render.
"""
# -*- coding: utf-8 -*-
from django_perseus.utils import find_renderers
from .renderers import AboutUsRenderer


def run_renderers(number=None):
    for render_cls in find_renderers():
        r = render_cls(number)
        r.generate()


def run_about_renderer():
    r = AboutUsRenderer()
    r.generate()
