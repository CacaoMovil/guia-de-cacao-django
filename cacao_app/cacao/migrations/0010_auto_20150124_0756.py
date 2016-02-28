# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cacao', '0009_auto_20150123_2143'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='content',
            unique_together=set([('peso', 'section')]),
        ),
    ]
