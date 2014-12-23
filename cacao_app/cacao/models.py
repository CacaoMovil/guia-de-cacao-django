# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse

class Guide(models.Model):
    """docstring for Guia"""
    number = models.IntegerField()
    name = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='cacao/')

    class Meta:
        verbose_name = "Guia"
        verbose_name_plural  = "Guias"
        ordering = ["number"]
            
    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('guia_detail', args=(self.pk,))

    def next(self):
        try:
            return Content.objects.get(pk=self.pk)
        except:
            return None

class Section(models.Model):
    """docstring for seccion"""
    guide = models.ForeignKey(Guide)
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='cacao/')

    class Meta:
        verbose_name = "Seccion"
        verbose_name_plural  = "Secciones"

    def __unicode__(self):
        return self.title

class Content(models.Model):
    """docstring for Contenido"""
    section = models.ForeignKey(Section, related_name='contenidos')
    title = models.CharField(max_length=250)
    description = models.TextField()
    peso = models.IntegerField("Peso del contenido")
    image = models.ImageField(upload_to='cacao/')

    class Meta:
        verbose_name = "Contenido"
        verbose_name_plural  = "Contenidos"

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('contenido_detail', args=(self.pk,))

    def next(self):
        try:
            return Content.objects.get(pk=self.pk+1)
        except:
            return None

    def previous(self):
        try:
            return Content.objects.get(pk=self.pk-1)
        except:
            return None

    @property
    def guide(self):
        return self.section.guide

class Download(models.Model):
    """docstring for Descargas"""
    download = models.FileField(upload_to='descargas/')