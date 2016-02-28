# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cacao', '0008_auto_20150123_2115'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='content',
            options={'ordering': ['peso'], 'verbose_name': 'Contenido', 'verbose_name_plural': 'Contenidos'},
        ),
        migrations.AlterField(
            model_name='content',
            name='peso',
            field=models.PositiveIntegerField(help_text=b'Entre mayor sea el peso mas al fondo se ubica', verbose_name=b'Peso del Contenido'),
            preserve_default=True,
        ),
    ]
