# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountryEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('event', models.ForeignKey(to='event.Event')),
            ],
            options={
                'verbose_name': 'Evento',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='event',
            name='country',
        ),
    ]
