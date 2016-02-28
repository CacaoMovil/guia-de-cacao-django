# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from .views import PDFDownloadView

urlpatterns = patterns('',  # noqa
    url(r'^download/$', PDFDownloadView.as_view(), name='download'),
)
