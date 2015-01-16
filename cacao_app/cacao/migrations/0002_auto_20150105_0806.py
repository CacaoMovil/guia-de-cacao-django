# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cacao', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='peso',
            field=models.PositiveIntegerField(unique=True, verbose_name=b'Peso del contenido'),
            preserve_default=True,
        ),
    ]
