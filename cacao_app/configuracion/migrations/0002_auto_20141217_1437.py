# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='acerca',
            options={'verbose_name': 'Configuracion Acerca'},
        ),
        migrations.AlterModelOptions(
            name='contacto',
            options={'verbose_name': 'Configuracion Contacto'},
        ),
        migrations.AddField(
            model_name='acerca',
            name='informacion_bienvenida',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contacto',
            name='contacto_general',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contacto',
            name='informacion_contacto',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
