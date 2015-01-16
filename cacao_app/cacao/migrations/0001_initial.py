# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('peso', models.IntegerField(verbose_name=b'Peso del contenido')),
                ('image', models.ImageField(upload_to=b'cacao/')),
            ],
            options={
                'verbose_name': 'Contenido',
                'verbose_name_plural': 'Contenidos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Download',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('download', models.FileField(upload_to=b'descargas/')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField()),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to=b'cacao/')),
            ],
            options={
                'ordering': ['number'],
                'verbose_name': 'Guia',
                'verbose_name_plural': 'Guias',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to=b'cacao/')),
                ('guide', models.ForeignKey(to='cacao.Guide')),
            ],
            options={
                'verbose_name': 'Seccion',
                'verbose_name_plural': 'Secciones',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='content',
            name='section',
            field=models.ForeignKey(related_name='contenidos', to='cacao.Section'),
            preserve_default=True,
        ),
    ]
