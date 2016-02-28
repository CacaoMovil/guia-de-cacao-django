# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cacao', '0006_auto_20150119_0946'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='peso',
            field=models.PositiveIntegerField(default=1, help_text=b'Entre mayor sea el peso mas al fondo se ubica', verbose_name=b'Peso de la Seccion'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='content',
            name='description',
            field=models.TextField(verbose_name=b'Descripcion'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='content',
            name='image',
            field=models.ImageField(help_text=b'Required dimensions 1563x538', upload_to=b'cacao/', verbose_name=b'Imagen', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='content',
            name='peso',
            field=models.PositiveIntegerField(unique=True, verbose_name=b'Peso del Contenido'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='content',
            name='title',
            field=models.CharField(max_length=250, verbose_name=b'Titulo'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='guide',
            name='description',
            field=models.TextField(verbose_name=b'Descripcion'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='guide',
            name='image',
            field=models.ImageField(upload_to=b'cacao/', verbose_name=b'Imagen'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='guide',
            name='name',
            field=models.CharField(max_length=250, verbose_name=b'Nombre'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='guide',
            name='number',
            field=models.IntegerField(verbose_name=b'Numero'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='section',
            name='image',
            field=models.ImageField(upload_to=b'cacao/', verbose_name=b'Imagen', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='section',
            name='title',
            field=models.CharField(max_length=250, verbose_name=b'Titulo'),
            preserve_default=True,
        ),
    ]
