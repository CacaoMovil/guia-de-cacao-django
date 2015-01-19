# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import Max
from django.conf import settings
from django.core.urlresolvers import reverse
from django.template import defaultfilters
from django.template.base import add_to_builtins

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

    def get_download_url(self):
        try:
            download = Download.objects.filter(guide=self.pk).order_by('-num_version')[0]
            return download.file.url
        except:
            return None

    def next(self):
        try:
            return Content.objects.get(pk=self.pk)
        except:
            return None

    @property
    def latest_version(self):
        try:
            return self.versions.order_by('-num_version')[0]
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
    extract = models.CharField("Extracto del Contenido",max_length=250)
    description = models.TextField()
    peso = models.PositiveIntegerField("Peso del contenido", unique=True)
    image = models.ImageField(upload_to='cacao/', help_text="Required dimensions 1563x538")
    slug = models.SlugField(max_length=100)

    class Meta:
        verbose_name = "Contenido"
        verbose_name_plural  = "Contenidos"

    def __unicode__(self):
        return self.title


    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(self.title)
        super(Content, self).save(*args, **kwargs)

    def get_absolute_url(self):
        guide = self.section.guide.pk
        return reverse('contenido_detail', args=[guide, self.slug])

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
    guide = models.ForeignKey(Guide, related_name='versions')
    file = models.FileField(upload_to='descargas/')
    num_version = models.PositiveIntegerField()
    # No Visible
    date = models.DateField(auto_now_add=True, editable=False)
    name = models.CharField(max_length=250)


    class Meta:
        verbose_name = "Descarga"
        verbose_name_plural = "Descargas"
        unique_together = ("guide", "num_version")

    def __unicode__(self):
        return self.guide.name

    def save(self, *args, **kwargs):
        self.name = self.guide.name
        super(Download, self).save(*args, **kwargs)

    def get_last_version(self, number):
        try:
            last_version = Download.objects.filter(guide__number=number).aggregate(Max('num_version'))
            return last_version.get('num_version__max') + 1
        except:
            last_version = 1
            return last_version

### Monkey Patch

if getattr(settings, 'USE_PERSEUS', False):
    add_to_builtins('cacao.templatetags.django_perseus_tags')
else:
    add_to_builtins('django.templatetags.static')


