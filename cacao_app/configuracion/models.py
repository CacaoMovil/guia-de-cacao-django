# -*- coding: utf-8 -*-
from django.db import models
from solo.models import SingletonModel

class Contacto(SingletonModel):
    informacion_contacto = models.TextField()
    contacto_general = models.TextField()

    class Meta:
        verbose_name = "Configuracion Contacto"

class Acerca(SingletonModel):
    informacion_bienvenida = models.TextField()

    class Meta:
        verbose_name = "Configuracion Acerca"