# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Event


class EventAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_filter = ('start', 'end', 'country')
    list_display = ('name', 'country', 'start', 'end')

admin.site.register(Event, EventAdmin)
