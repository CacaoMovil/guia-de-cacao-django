"""
This command render all the stored
elements

** Example:
    python manage.py render_all --configuration=Export
    --archive
"""
# -* coding: utf-8 -*-
import logging
from os import remove as rm
from os.path import join
from shutil import move

from optparse import make_option

from django.conf import settings
from django.core.management.base import BaseCommand
from django.core.cache import get_cache

from django_perseus.utils import run_importers

from cacao.utils import run_renderers

from .render_guia import zip_dir


logger = logging.getLogger('perseus')
cache = get_cache('default')


class Command(BaseCommand):
    help = 'Render all elements'
    cache.delete('media_urls')
    cache.delete('static_urls')

    option_list = BaseCommand.option_list + (
        make_option('--archive',
                    action='store_true',
                    dest='archive',
                    default=False,
                    help='Zips the result of the statically generated website'),  # noqa

    )

    def handle(self, *args, **options):
        # first render all elements
        run_renderers()
        run_importers()
        # make the folder zip
        if options.get('archive'):
                zip_dir('guia-de-cacao-completa.zip', '1', '1')

        # move from tmp to media
        try:
            rm(join(settings.MEDIA_ROOT, 'guia-de-cacao-completa.zip'))  # noqa
        except:
            pass
        move(join(settings.PERSEUS_BUILD_DIR, 'guia-de-cacao-completa.zip'), settings.MEDIA_ROOT)  # noqa
