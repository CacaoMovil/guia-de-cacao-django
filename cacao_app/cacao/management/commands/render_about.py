"""
This Command is based in Django Perseus Command,
but with super powers and Kronoscode magic.
"""
# -*- coding: utf-8 -*-
from optparse import make_option

from django.conf import settings
from django.core.management.base import BaseCommand
from django.core.cache import get_cache

from django_perseus.utils import run_importers

from cacao.utils import run_about_renderer

import logging
import os
import zipfile

logger = logging.getLogger('perseus')
cache = get_cache('default')

class Command(BaseCommand):
    help = 'Renders about us page'
    cache.delete('media_urls')
    cache.delete('static_urls')

    def handle(self, *args, **options):
        run_about_renderer()
        run_importers()

