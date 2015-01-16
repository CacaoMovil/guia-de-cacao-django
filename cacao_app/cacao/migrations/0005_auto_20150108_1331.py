# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cacao', '0004_auto_20150108_1003'),
    ]

    operations = [
        migrations.AddField(
            model_name='download',
            name='num_version',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='download',
            unique_together=set([('guide', 'num_version')]),
        ),
    ]
