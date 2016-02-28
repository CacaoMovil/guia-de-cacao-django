# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cacao', '0010_auto_20150124_0756'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='download',
            options={'ordering': ['-num_version'], 'verbose_name': 'Descarga', 'verbose_name_plural': 'Descargas'},
        ),
        migrations.AddField(
            model_name='download',
            name='checksum',
            field=models.CharField(max_length=32, editable=False, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='content',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name=b'Descripcion'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='download',
            name='file',
            field=models.FileField(null=True, upload_to=b'descargas/'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='download',
            name='guide',
            field=models.ForeignKey(related_name='versions', verbose_name=b'Guia', to='cacao.Guide'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='download',
            name='name',
            field=models.CharField(max_length=250, verbose_name=b'Nombre'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='guide',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name=b'Descripcion'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='guide',
            name='number',
            field=models.IntegerField(unique=True, verbose_name=b'Numero'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='section',
            name='guide',
            field=models.ForeignKey(verbose_name=b'Guia', to='cacao.Guide'),
            preserve_default=True,
        ),
    ]
