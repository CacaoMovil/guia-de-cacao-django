"""
This command render all the stored
elements

** Example:
    python manage.py render_all --configuration=Export
    --archive
"""
# -* coding: utf-8 -*-
import logging
from os import remove
from os import walk, mkdir
from os.path import join, isdir
from shutil import move, rmtree

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

    def handle_dirs(self):
        content_dir = join(settings.PERSEUS_SOURCE_DIR, 'contenido')
        # check if 'contenido' dir exists
        if isdir(content_dir):
            # remove the dir
            rmtree(content_dir)
        # create the 'contenido' dir
        mkdir(content_dir)
        # exclude some dir from path
        exclude = set(['static', 'contenido'])
        for dirname, dirnames, filenames in walk(settings.PERSEUS_SOURCE_DIR, topdown=True):  # noqa

            dirnames[:] = [d for d in dirnames if d not in exclude]
            for filename in filenames:
                if not filename == 'index.html':
                    move(join(dirname, filename), content_dir)

        move(join(settings.PERSEUS_SOURCE_DIR, 'static'), content_dir)

    def handle(self, *args, **options):

        # first render all elements
        run_renderers()
        run_importers()

        # move the dirs
        self.handle_dirs()

        # make the folder zip
        if options.get('archive'):
            zip_dir('guia-de-cacao-completa.zip')

            # move from tmp to media
            try:
                remove(join(settings.MEDIA_ROOT, 'guia-de-cacao-completa.zip'))  # noqa
            except:
                pass
            move(join(settings.PERSEUS_BUILD_DIR, 'guia-de-cacao-completa.zip'), settings.MEDIA_ROOT)  # noqa
