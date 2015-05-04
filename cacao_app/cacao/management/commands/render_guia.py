"""
This Command is based in Django Perseus Command,
but with super powers and Kronoscode magic.
"""
# -*- coding: utf-8 -*-
from optparse import make_option

from django.core.management.base import BaseCommand
from django.core.cache import get_cache

from django_perseus.utils import run_importers, zip_dir

from cacao.utils import run_renderers

cache = get_cache('default')

class Command(BaseCommand):
    help = 'Make a render from the specific element'
    cache.delete('media_urls')
    cache.delete('static_urls')

    option_list = BaseCommand.option_list + (
        make_option('--archive',
        action='store_true',
        dest='archive',
        default=False,
        help='Zips the result of the statically generated website'),

        make_option('--filename',
        action='store',
        dest='filename',
        default='',
        help='Name of the file to zip'),

        make_option('--element',
        action='store',
        dest='element',
        default=False,
        type=int,
        help='Number of element to render and zip'),
    )

    def handle(self, *args, **options):

        if options['element']:
            run_renderers(options.get('element'))
        else:
            run_renderers()

        run_importers()

        if options['archive']:
            zip_dir(options.get('filename', 'render.zip'))
