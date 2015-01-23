# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.forms import ModelForm

from suit_ckeditor.widgets import CKEditorWidget

from .models import Guide, Section, Content, Download


class GuideForm(ModelForm):
    class Meta:
        model = Guide

        _ck_editor_toolbar = [
            {'name': 'basicstyles', 'groups': ['basicstyles', 'cleanup', 'undo', 'clipboard']},
            {'name': 'paragraph',
             'groups': ['list', 'indent', 'blocks', 'align']},
            {'name': 'document', 'groups': ['mode']}, '/',
            {'name': 'styles'}, {'name': 'colors'},
            {'name': 'insert_custom',
             'items': ['Image', 'Flash', 'Table', 'HorizontalRule']}]

        _ck_editor_config = {'autoGrow_onStartup': True,
                             'autoGrow_minHeight': 100,
                             'autoGrow_maxHeight': 250,
                             'extraPlugins': 'autogrow',
                             'toolbarGroups': _ck_editor_toolbar}

        widgets = {
            'description': CKEditorWidget(editor_options=_ck_editor_config),
        }
    

class GuideAdmin(ModelAdmin):
    form = GuideForm
    search_fields = ('number', 'name')
    list_display = ('name', 'number')
    fieldsets = [
      (None, {
        'fields': ['number', 'name', 'description', 'image']}
      )
    ]

class ContentForm(ModelForm):
    class Meta:
        model = Content

        _ck_editor_toolbar = [
            {'name': 'basicstyles', 'groups': ['basicstyles', 'cleanup', 'undo', 'clipboard']},
            {'name': 'paragraph',
             'groups': ['list', 'indent', 'blocks', 'align']},
            {'name': 'document', 'groups': ['mode']}, '/',
            {'name': 'styles'}, {'name': 'colors'},
            {'name': 'insert_custom',
             'items': ['Image', 'Flash', 'Table', 'HorizontalRule']}]

        _ck_editor_config = {'autoGrow_onStartup': True,
                             'autoGrow_minHeight': 100,
                             'autoGrow_maxHeight': 250,
                             'extraPlugins': 'autogrow',
                             'toolbarGroups': _ck_editor_toolbar}

        widgets = {
            'description': CKEditorWidget(editor_options=_ck_editor_config),
        }

class ContentAdmin(ModelAdmin):
    form = ContentForm
    search_fields = ('title',)
    list_filter = ('section',)
    list_display = ('title', 'section')
    fieldsets = [
      (None, {
        'fields': ['section', 'title', 'extract', 'description', 'peso', 'image']}
      )
    ]

class SectionAdmin(admin.ModelAdmin):
    model = Section
    #inlines = [ContentForm, ContentAdmin]
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
admin.site.register(Content, ContentAdmin)
admin.site.register(Download, DownloadAdmin)
