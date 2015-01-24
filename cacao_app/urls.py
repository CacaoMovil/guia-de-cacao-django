# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

from cacao.views import render_element

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^how-it-works/$',
        TemplateView.as_view(template_name='how_works.html'),
        name="how_it_works"),

    url(r'^admin/static-generator/$', render_element),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # User management
    #url(r'^users/', include("users.urls", namespace="users")),
    url(r'^accounts/', include('allauth.urls')),

    # Uncomment the next line to enable avatars
    url(r'^avatar/', include('avatar.urls')),

    # Your stuff: custom urls go here
    url(r'', include('cacao.urls')),
    url(r'', include('configuracion.urls')),
    url(r'^ckeditor/', include('ckeditor.urls')),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
