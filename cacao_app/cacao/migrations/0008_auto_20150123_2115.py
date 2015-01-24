# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cacao', '0007_auto_20150123_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='title_content',
            field=models.CharField(default='test', max_length=250, verbose_name=b'Titulo Contenido'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='content',
            name='title',
            field=models.CharField(max_length=250, verbose_name=b'Titulo Menu'),
            preserve_default=True,
        ),
    ]
