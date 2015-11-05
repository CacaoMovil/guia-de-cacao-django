# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import hashlib
import os
from os.path import join, dirname, abspath
from django.db import models, migrations


BASE_DIR = dirname(dirname(abspath(__file__)))
MEDIA_ROOT = join(BASE_DIR, 'media')


def create_checksum(file_path):
    """
    Same method in Download Model
    """
    hash = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash.update(chunk)
    return hash.hexdigest()


def build_old_checksum(apps, schema_editor):
    Download = apps.get_model("cacao", "Download")

    for download in Download.objects.all():
        zip_path = os.path.join(MEDIA_ROOT, str(download.file))
        try:
            download.checksum = create_checksum(zip_path)
            download.save()
        except:
            pass


class Migration(migrations.Migration):

    dependencies = [
        ('cacao', '0011_auto_20151022_1058'),
    ]

    operations = [
        migrations.RunPython(build_old_checksum)
    ]

