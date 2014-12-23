# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from .views import GuideList, GuideDetail, ContentDetail

urlpatterns = patterns('cacao.views',
    url(r'^$', GuideList.as_view(), name="home"),
    url(r'^guia/(?P<pk>\d+)/$', GuideDetail.as_view(), name="guia_detail"),
    url(r'^contenido/(?P<pk>\d+)/$', ContentDetail.as_view(), name="contenido_detail"),
)