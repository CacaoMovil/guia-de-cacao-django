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
    url(r'^guia/(?P<guide>\d)/contenido/(?P<slug>[-\w]+)/$', ContentDetail.as_view(), name="contenido_detail"),
    url(r'^static-generator/$', 'staticGenerator', name="static_generator"),

    # api
    url(r'^api/v1/guides/$', 'guides_collection'),
    url(r'^api/v1/guide/(?P<pk>[0-9]+)$', 'guide_elements'),
    url(r'^api/v1/guide/(?P<pk>[0-9]+)/version/(?P<num_version>[0-9]+)$', 'guide_element'),
    url(r'^api/v1/guide/(?P<pk>[0-9]+)/last$', 'guide_last'),
)