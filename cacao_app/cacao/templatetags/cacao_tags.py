
from django import template
from django.conf import settings

register = template.Library()

@register.filter
def offline_media(value):
    if getattr(settings, "USE_PERSEUS", False):
        return value.replace('/media/', 'static/')
    else:
        return value
