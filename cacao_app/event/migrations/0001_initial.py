# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250, verbose_name=b'Nombre')),
                ('description', ckeditor.fields.RichTextField(verbose_name=b'Descripcion')),
                ('start', models.DateTimeField(verbose_name=b'Inicio')),
                ('end', models.DateTimeField(verbose_name=b'Fin')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name=b'Creado')),
                ('country', django_countries.fields.CountryField(max_length=2)),
            ],
            options={
                'ordering': ['created_on'],
                'verbose_name': 'Evento',
                'verbose_name_plural': 'Eventos',
            },
            bases=(models.Model,),
        ),
    ]
