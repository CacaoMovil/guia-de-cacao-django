# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import patterns, url

from .views import GuideList, GuideDetail, ContentDetail

urlpatterns = patterns('cacao.views',
    url(r'^$', GuideList.as_view(), name="home"),

    url(r'^guia/(?P<guide_number>\d+)/$',
        GuideDetail.as_view(), name="guia_detail"),
    url(r'^guia/(?P<guide_number>\d+)/contenido/(?P<slug>[-\w]+)/$',
        ContentDetail.as_view(), name="contenido_detail"),
    url(r'^guia/descargas/guia(?P<guide_number>\d+)-version(?P<version>\d+).zip$', 'download_guide', name="download_guide"),  # noqa

    url(r'^render/$', 'render_element', name="render_element"),

    # api
    url(r'^api/v1/guides/$', 'guides_collection'),
    url(r'^api/v1/guide/(?P<number>\d+)/$', 'guide_elements'),
    url(r'^api/v1/guide/(?P<number>\d+)/version/(?P<num_version>\d+)/$', 'guide_element'),  # noqa
    url(r'^api/v1/guide/(?P<number>\d+)/last/$', 'guide_last'),
    url(r'^api/v1/settings/$', 'app_settings'),
)

if settings.USE_PERSEUS:
    urlpatterns += (
        url(r'^static_index/$',
            GuideList.as_view(template_name='index_static.html'),
            name="home_static"),
    )
