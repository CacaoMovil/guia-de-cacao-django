# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0002_auto_20141217_1437'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='acerca',
            options={'verbose_name': 'Configuracion de "Acerca de"'},
        ),
        migrations.AlterField(
            model_name='acerca',
            name='informacion_bienvenida',
            field=ckeditor.fields.RichTextField(verbose_name=b'Informacion de Bienvenida'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contacto',
            name='contacto_general',
            field=ckeditor.fields.RichTextField(verbose_name=b'Contacto General'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contacto',
            name='informacion_contacto',
            field=ckeditor.fields.RichTextField(verbose_name=b'Informacion de Contacto'),
            preserve_default=True,
        ),
    ]
