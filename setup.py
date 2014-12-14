# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import guia-de-cacao-django
version = guia-de-cacao-django.__version__

setup(
    name='Cacao',
    version=version,
    author='',
    author_email='kronos@kronoscode.com',
    packages=[
        'guia-de-cacao-django',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.7',
    ],
    zip_safe=False,
    scripts=['guia-de-cacao-django/manage.py'],
)
