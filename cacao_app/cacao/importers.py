"""
Django Perseus media importers, this get specific
static or media files and move to the deploy dir
"""
# -*- coding: utf-8 -*-
import os

from django_perseus.importers.base import BaseImporter
from django.core.cache import get_cache

from django_perseus.exceptions import ImporterException

cache = get_cache('default')


class MediaImporter(BaseImporter):

    """
    This class import the media files
    """
    target_dir = 'PERSEUS_STATIC_DIR'
    source_dir = 'MEDIA_ROOT'
    sub_dirs = []

    def __init__(self):
        self.sub_dirs += cache.get('media_urls') or []
        super(MediaImporter, self).__init__()


class StaticImporter(BaseImporter):

    """
    This class import the static files
    """
    target_dir = 'PERSEUS_STATIC_DIR'
    source_dir = 'STATIC_ROOT'
    sub_dirs = [
        'font',
        'css/icons/',
        'image/stellar/background2.jpg',
        'css/merriweathersans.css',
        'image/logo/vaina-cacao.png',
    ]

    def __init__(self):
        self.sub_dirs += cache.get('static_urls') or []
        super(StaticImporter, self).__init__()
