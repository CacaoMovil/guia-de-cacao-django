# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cacao', '0003_content_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='download',
            options={'verbose_name': 'Descarga', 'verbose_name_plural': 'Descargas'},
        ),
        migrations.RenameField(
            model_name='download',
            old_name='download',
            new_name='file',
        ),
        migrations.AddField(
            model_name='download',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 1, 8, 18, 1, 16, 31514, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='download',
            name='guide',
            field=models.ForeignKey(default=1, to='cacao.Guide'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='download',
            name='name',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]
