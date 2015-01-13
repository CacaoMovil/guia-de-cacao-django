# -*- coding: utf-8 -*-
from django_perseus.importers.base import BaseImporter

class MediaImporter(BaseImporter):

    target_dir = 'PERSEUS_STATIC_DIR'
    source_dir = 'MEDIA_ROOT'
    sub_dirs = [
        'cache',
        'cacao',
    ]

class StaticImporter(BaseImporter):
    target_dir = 'PERSEUS_STATIC_DIR'
    source_dir = 'STATIC_ROOT'
    sub_dirs = [
        'css',
        'font',
        'js',
        'image'
    ]
