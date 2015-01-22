'''
Django Perseus Config
'''
# -*- coding: utf-8 -*-
import os
from os.path import join, dirname

from .production import Production

BASE_DIR = dirname(dirname(__file__))

class Local(Production):
    USE_PERSEUS = True
    DEBUG = True
    RENDER_STATIC = True
    PERSEUS_BUILD_DIR = '/tmp/perseus/build'
    PERSEUS_SOURCE_DIR = '/tmp/perseus/_output'
    PERSEUS_STATIC_DIR = os.path.join(
        PERSEUS_SOURCE_DIR, "static"
    )
    PERSEUS_IMPORTERS = [
        'cacao.importers.MediaImporter',
        'cacao.importers.StaticImporter',
    ]
    MEDIA_URL = 'static/'
