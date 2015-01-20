# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cacao', '0005_auto_20150108_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='extract',
            field=models.CharField(default='test', max_length=250, verbose_name=b'Extracto del Contenido'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='content',
            name='image',
            field=models.ImageField(help_text=b'Required dimensions 1563x538', upload_to=b'cacao/'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='download',
            name='guide',
            field=models.ForeignKey(related_name='versions', to='cacao.Guide'),
            preserve_default=True,
        ),
    ]
