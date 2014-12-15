# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import cacao_app
version = cacao_app.__version__

setup(
    name='cacao_app',
    version=version,
    author='',
    author_email='info@kronoscode.com',
    packages=[
        'cacao_app',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.7',
    ],
    zip_safe=False,
    scripts=['cacao_app/manage.py'],
)
