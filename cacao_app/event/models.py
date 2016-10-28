# -*- coding: utf-8 -*-

from django.db import models

from ckeditor.fields import RichTextField
from django_countries.fields import CountryField


class Event(models.Model):
    name = models.CharField('Nombre', max_length=250)
    description = RichTextField('Descripcion', config_name='default')
    start = models.DateTimeField('Inicio')
    end = models.DateTimeField('Fin')
    created_on = models.DateTimeField('Creado', auto_now_add=True)
    country = CountryField()

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
        ordering = ['created_on']

    def __unicode__(self):
        return self.name
