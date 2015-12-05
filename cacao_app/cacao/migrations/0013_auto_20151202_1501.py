# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('cacao', '0012_auto_20151022_1529'),
    ]

    operations = [
        migrations.AddField(
            model_name='guide',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='download',
            name='checksum',
            field=models.CharField(max_length=32, blank=True),
            preserve_default=True,
        ),
    ]
