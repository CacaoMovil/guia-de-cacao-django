# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse

class Guia(models.Model):
    """docstring for Guia"""
    numero = models.IntegerField()
    nombre = models.CharField(max_length=250)
    descripcion = models.TextField()
    imagen_portada = models.ImageField(upload_to='cacao/')

    class Meta:
        verbose_name = "Guia"
        verbose_name_plural  = "Guias"
        ordering = ["numero"]
            
    def __unicode__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('guia_detail', args=(self.pk,))

    def next(self):
        try:
            return Contenido.objects.get(pk=self.pk)
        except:
            return None

class Seccion(models.Model):
    """docstring for seccion"""
    guia = models.ForeignKey(Guia)
    titulo = models.CharField(max_length=250)
    foto_seccion = models.ImageField(upload_to='cacao/')

    class Meta:
        verbose_name = "Seccion"
        verbose_name_plural  = "Secciones"

    def __unicode__(self):
        return self.titulo

class Contenido(models.Model):
    """docstring for Contenido"""
    seccion = models.ForeignKey(Seccion, related_name='contenidos')
    titulo = models.CharField(max_length=250)
    contenido = models.TextField()
    peso = models.IntegerField("Peso del contenido")
    imagen_contenido = models.ImageField(upload_to='cacao/')

    class Meta:
        verbose_name = "Contenido"
        verbose_name_plural  = "Contenidos"

    def __unicode__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('contenido_detail', args=(self.pk,))

    def next(self):
        try:
            return Contenido.objects.get(pk=self.pk+1)
        except:
            return None

    def previous(self):
        try:
            return Contenido.objects.get(pk=self.pk-1)
        except:
            return None

    @property
    def guia(self):
        return self.seccion.guia

class Descarga(models.Model):
    """docstring for Descargas"""
    descarga = models.FileField(upload_to='descargas/')