"""
Custom template tag inspired in Django Perseus
but whit custom code that help us to convert basic url
to hashlib and make more easy the navigation
"""
# -*- coding: utf-8 -*-
import hashlib

from django import template
from django.conf import settings
from django.template.defaulttags import url as django_url_tag
from django.template.defaulttags import URLNode
from django.templatetags.static import do_static, StaticNode
from django.core.cache import get_cache

cache = get_cache('default')

register = template.Library()


def render_static():
    return getattr(settings, 'RENDER_STATIC', False)


class StaticUrlNode(StaticNode):

    def render(self, context):
        url = super(StaticUrlNode, self).render(context)
        return_value = url
        if not render_static():
            return url

        if url.startswith('/'):
            return_value = url[1:]

        static_urls = cache.get('static_urls') or []
        cleaned_value = return_value.replace('static/', '')
        if cleaned_value not in static_urls:
            static_urls.append(cleaned_value)
        cache.set('static_urls', static_urls)

        return return_value


@register.tag
def static(parser, token, node_cls=StaticUrlNode):
    node_instance = do_static(parser, token)

    return node_cls(
        varname=node_instance.varname,
        path=node_instance.path
    )


class RenderUrlNode(URLNode):

    path = '{0}.html'

    def render(self, context):
        base_url = super(RenderUrlNode, self).render(context)
        # Convert basic url to hash this is used for links
        url = hashlib.sha1(base_url).hexdigest()
        if not render_static():
            return url

        if url == '/':
            return self.path.format('index')

        if url.startswith('/'):
            url = url[1:]

        if url.endswith('/'):
            return self.path.format(url[:-1])
        else:
            return self.path.format(url)


@register.tag
def url(parser, token, node_cls=RenderUrlNode):
    node_instance = django_url_tag(parser, token)

    return node_cls(
        view_name=node_instance.view_name,
        args=node_instance.args,
        kwargs=node_instance.kwargs,
        asvar=node_instance.asvar
    )
