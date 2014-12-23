# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cacao', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Descargas',
            new_name='Descarga',
        ),
        migrations.AlterModelOptions(
            name='contenido',
            options={'verbose_name': 'Contenido', 'verbose_name_plural': 'Contenidos'},
        ),
        migrations.AlterModelOptions(
            name='guia',
            options={'verbose_name': 'Guia', 'verbose_name_plural': 'Guias'},
        ),
        migrations.AlterModelOptions(
            name='seccion',
            options={'verbose_name': 'Seccion', 'verbose_name_plural': 'Secciones'},
        ),
    ]
