# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.views import defaults as default_views

from cacao.views import render_element

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^como-funciona/$',
        TemplateView.as_view(template_name='how_works.html'),
        name="how_it_works"),

    url(r'^admin/static-generator/$', render_element),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^pdf-kit/', include('pdf_kit.urls', namespace='pdf-kit')),

    # Your stuff: custom urls go here
    url(r'', include('cacao.urls')),
    url(r'', include('configuracion.urls')),
    url(r'^ckeditor/', include('ckeditor.urls')),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += (
        url(r'^400/$', default_views.bad_request),
        url(r'^403/$', default_views.permission_denied),
        url(r'^404/$', default_views.page_not_found),
        url(r'^500/$', default_views.server_error),
    )
