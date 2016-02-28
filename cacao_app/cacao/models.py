# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import Max
from django.conf import settings
from django.core.urlresolvers import reverse
from django.template import defaultfilters
from django.template.base import add_to_builtins

from ckeditor.fields import RichTextField

class Guide(models.Model):
    """
    This model store the Guia objects
    """
    number = models.IntegerField('Numero', unique=True)
    name = models.CharField('Nombre', max_length=250)
    description = RichTextField('Descripcion', config_name='default')
    image = models.ImageField('Imagen', upload_to='cacao/')

    class Meta:
        verbose_name = 'Guia'
        verbose_name_plural  = 'Guias'
        ordering = ['number']

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('guia_detail', args=(self.number,))

    def get_download_url(self):
        try:
            download = Download.objects.filter(guide=self.number).order_by('-num_version')[0]
            return download.file.url
        except:
            return None

    def next_content(self):
        """
        Return First Content Of A Guide
        """
        try:
            return Content.objects.filter(section=self.section_set.all())[0]
        except:
            return None

    def next_section(self):
        """
        Return the next section of a guide of a guide pointing
        to the first Content of this section
        """
        try:
            return Content.objects.filter(section=self.section_set.all())[0]
        except:
            return None

    def previous_section(self):
        """
        Return the previous section of a guide pointing
        to the first Content of this section
        """
        try:
            return Content.objects.filter(section=self.section_set.all())[0]
        except:
            return None

    @property
    def latest_version(self):
        try:
            return self.versions.order_by('-num_version')[0]
        except:
            return None


class Section(models.Model):
    """
    This model store the Section object and have a
    relationship with the Guide model because every
    Guide have many sections
    """
    guide = models.ForeignKey(Guide)
    title = models.CharField('Titulo', max_length=250)
    peso = models.PositiveIntegerField("Peso de la Seccion", help_text='Entre mayor sea el peso mas al fondo se ubica')
    image = models.ImageField('Imagen', upload_to='cacao/', blank=True)

    class Meta:
        verbose_name = 'Seccion'
        verbose_name_plural  = 'Secciones'

    def __unicode__(self):
        return "%s - Guia: %s" %(self.title, self.guide)

    def next(self):
        """
        return the next section
        """
        try:
            return Section.objects.filter(peso__gt=self.peso, guide=self.guide)[0]
        except Exception, e:
            raise e

    def previous(self):
        """
        return the previous section
        """
        try:
            return Section.objects.filter(peso__lt=self.peso, guide=self.guide)[0]
        except Exception, e:
            raise e

class Content(models.Model):
    """
    This model store the Contenido object and have a
    relationshipwith the Section model because every
    Content have many Sections
    """
    section = models.ForeignKey(Section, related_name='contenidos')
    title = models.CharField('Titulo Menu', max_length=250)
    title_content = models.CharField('Titulo Contenido', max_length=250)
    extract = models.CharField("Extracto del Contenido", max_length=250)
    description = RichTextField('Descripcion', config_name='default')
    peso = models.PositiveIntegerField("Peso del Contenido", help_text='Entre mayor sea el peso mas al fondo se ubica')
    image = models.ImageField('Imagen', upload_to='cacao/', help_text='Required dimensions 1563x538', blank=True)
    slug = models.SlugField(max_length=100)

    class Meta:
        verbose_name = 'Contenido'
        verbose_name_plural  = 'Contenidos'
        ordering = ['peso']
        unique_together = ('peso', 'section')

    def __unicode__(self):
        return self.title


    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(self.title)
        super(Content, self).save(*args, **kwargs)

    def get_absolute_url(self):
        guide = self.section.guide.number
        return reverse('contenido_detail', args=[guide, self.slug])

    def next(self):
        """
        return the next Content
        """
        try:
            return Content.objects.filter(peso__gt=self.peso, section=self.section)[0]
        except IndexError:
            try:
                return Content.objects.filter(section=self.section.next())[0]
            except:
                return None

    def previous(self):
        """
        return the previous Content
        """
        try:
            return Content.objects.filter(peso__lt=self.peso, section=self.section)[0]
        except IndexError:
            try:
                return Content.objects.filter(section=self.section.previous())[0]
            except:
                return None

    @property
    def guide(self):
        return self.section.guide

class Download(models.Model):
    """
    This model store the Descargas object and have
    a relationship with Guide because a Download file
    belongs to a Guide object
    """
    guide = models.ForeignKey(Guide, related_name='versions')
    file = models.FileField(upload_to='descargas/')
    num_version = models.PositiveIntegerField()
    # No Visible
    date = models.DateField(auto_now_add=True, editable=False)
    name = models.CharField(max_length=250)

    class Meta:
        verbose_name = 'Descarga'
        verbose_name_plural = 'Descargas'
        unique_together = ('guide', 'num_version')

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
