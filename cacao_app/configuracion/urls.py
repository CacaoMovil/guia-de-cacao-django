# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import patterns, url

from .views import AboutView, Contact

urlpatterns = patterns('configuracion.views',
	url(r'^acerca-de/$', AboutView.as_view(), name="about"),
	url(r'^contacto/', Contact.as_view(), name="envelope-contact"),
)