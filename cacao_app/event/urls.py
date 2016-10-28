# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import patterns, url

urlpatterns = patterns('event.views',
    url(r'^api/v1/events/$', 'events_collection'),
    url(r'^api/v1/events/(?P<country_code>[-_\w]+)/$', 'events_per_country'),
)
