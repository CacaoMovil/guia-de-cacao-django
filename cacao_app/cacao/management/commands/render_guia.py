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

from cacao.utils import run_renderers

import logging
import os
import zipfile

logger = logging.getLogger('perseus')
cache = get_cache('default')


def zip_dir(file_name, number=None, version=None):
    source_dir = getattr(settings, 'PERSEUS_SOURCE_DIR', None)
    if not source_dir:
        raise Exception('PERSEUS_SOURCE_DIR not defined in settings')

    if not os.path.isdir(source_dir):
        raise Exception('PERSEUS_SOURCE_DIR is not a valid directory')

    build_dir = getattr(settings, 'PERSEUS_BUILD_DIR', None)
    if not build_dir:
        raise Exception('PERSEUS_BUILD_DIR not defined in settings.')

    if not os.path.isdir(build_dir):
        os.makedirs(build_dir)

    rel_path = os.path.abspath(os.path.join(source_dir, os.pardir))

    file_path = os.path.abspath(os.path.join(build_dir, file_name))
    zip_file = zipfile.ZipFile(file_path, 'w')
    for root, dirs, files in os.walk(source_dir):
        for _file in files:
            location = os.path.join(root, _file)
            # path for file in zip archive
            if number and version:
                new_root = root.replace('/guia', '/guia%s-version%s' % (number, version))  # noqa
            else:
                new_root = root.replace('/guia', '/guia-cacao')  # noqa
            zip_name = os.path.join(os.path.relpath(new_root, rel_path), _file)
            zip_file.write(location, arcname=zip_name)
            logger.debug('File: {0} added to {1}'.format(zip_name, file_name))
    zip_file.close()


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
        make_option('--guide-version',
                    action='store',
                    dest='guide_version',
                    default=False,
                    type=int,
                    help='Number of element to render and zip'),

    )

    def handle(self, *args, **options):

        if options.get('element') and options.get('guide_version'):
            element = options.get("element")
            guide_version = options.get("guide_version")
            run_renderers(options.get('element'))
            run_importers()

            if options.get('archive'):
                zip_dir(options.get('filename', 'render.zip'), element, guide_version)
        else:
            raise Exception("element and guide-version are required")
