# -*- coding: utf-8 -*-
from django.db import models

from solo.models import SingletonModel
from ckeditor.fields import RichTextField

class Contacto(SingletonModel):
    """
    This model store the Contacto object
    but this only have one instance
    """
    informacion_contacto = RichTextField('Informacion de Contacto', config_name='default')
    contacto_general = RichTextField('Contacto General', config_name='default')

    class Meta:
        verbose_name = "Configuracion Contacto"

class Acerca(SingletonModel):
    """
    This model store the Contacto object
    but this only have one instance
    """
    informacion_bienvenida = RichTextField('Informacion de Bienvenida', config_name='default')

    class Meta:
        verbose_name = "Configuracion Acerca"
