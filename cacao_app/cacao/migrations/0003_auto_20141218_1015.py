# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cacao', '0002_auto_20141215_1533'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='guia',
            options={'ordering': ['numero'], 'verbose_name': 'Guia', 'verbose_name_plural': 'Guias'},
        ),
        migrations.AddField(
            model_name='contenido',
            name='peso',
            field=models.IntegerField(default=1, verbose_name=b'Peso del contenido'),
            preserve_default=False,
        ),
    ]
