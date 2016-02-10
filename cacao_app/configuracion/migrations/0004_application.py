# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0003_auto_20151022_1106'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250, verbose_name=b'Titulo')),
                ('sub_title', models.CharField(max_length=250, verbose_name=b'Sub Titulo')),
                ('logo', models.ImageField(upload_to=b'cacao/', verbose_name=b'Imagen')),
            ],
            options={
                'verbose_name': 'Configuracion de Aplicaci\xf3n',
            },
            bases=(models.Model,),
        ),
    ]
