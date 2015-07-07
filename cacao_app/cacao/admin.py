# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Guide, Section, Content, Download


class GuideAdmin(ModelAdmin):
    search_fields = ('number', 'name')
    list_display = ('name', 'number')
    fieldsets = [
        (None, {
            'fields': ['number', 'name', 'description', 'image']}
         )
    ]


class ContentInline(admin.StackedInline):
    model = Content
    exclude = ('slug',)
    extra = 1


class SectionAdmin(admin.ModelAdmin):
    model = Section
    inlines = [ContentInline, ]
    search_fields = ('title',)
    list_filter = ('title', 'guide')
    list_display = ('title', 'guide')


class DownloadAdmin(admin.ModelAdmin):
    model = Download
    search_fields = ('guide',)
    list_filter = ('guide',)
    list_display = ('name', 'num_version', 'guide')
    fieldsets = [
        (None, {
            'fields': ['guide', 'num_version', 'file']}
         )
    ]

admin.site.register(Guide, GuideAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Download, DownloadAdmin)
