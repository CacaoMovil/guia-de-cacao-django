# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contenido',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=250)),
                ('contenido', models.TextField()),
                ('imagen_contenido', models.ImageField(upload_to=b'cacao/')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Descargas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descarga', models.FileField(upload_to=b'descargas/')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Guia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.IntegerField()),
                ('nombre', models.CharField(max_length=250)),
                ('descripcion', models.TextField()),
                ('imagen_portada', models.ImageField(upload_to=b'cacao/')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Seccion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=250)),
                ('foto_seccion', models.ImageField(upload_to=b'cacao/')),
                ('guia', models.ForeignKey(to='cacao.Guia')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='contenido',
            name='seccion',
            field=models.ForeignKey(to='cacao.Seccion'),
            preserve_default=True,
        ),
    ]
