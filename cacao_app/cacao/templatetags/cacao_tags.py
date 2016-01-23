from pyquery import PyQuery as pq

from django import template
from django.conf import settings
from django.core.cache import get_cache
cache = get_cache('default')

register = template.Library()


@register.simple_tag
def settings_value(name):
    '''
    {% settings_value "LANGUAGE_CODE" %}
    '''
    return getattr(settings, name, "")


@register.filter
def offline_media(value):
    if getattr(settings, "USE_PERSEUS", False):
        new_val = value.replace('/media/', 'static/')
        imgs = pq(new_val)('img')
        media_urls = cache.get('media_urls') or []
        for img in imgs:
            src = pq(img).attr('src').replace('static/', '')
            if src not in media_urls:
                media_urls.append(src)
        cache.set('media_urls', media_urls)
        return new_val
    else:
        return value
