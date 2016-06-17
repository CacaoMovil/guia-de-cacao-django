# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Guide, Download


class DownloadSerializer(serializers.ModelSerializer):

    """
    Serializers for guide element, guide versions
    and last guide
    """
    file = serializers.SerializerMethodField('get_alternate_name')
    tags = serializers.SerializerMethodField('get_guide_tags')

    class Meta:
        model = Download
        fields = ('name', 'file', 'date', 'num_version', 'tags')

    def get_alternate_name(self, obj):
        try:
            return self.context['request'].build_absolute_uri(obj.get_download_url())  # noqa
        except:
            return ''

    def get_guide_tags(self, obj):
        return ','.join([t.name for t in obj.guide.tags.all()])


class GuidesSerializer(serializers.ModelSerializer):

    """
    Serializers for list all guides
    """
    date = serializers.SerializerMethodField('latest_guide_date')
    file = serializers.SerializerMethodField('guide_file')
    num_version = serializers.SerializerMethodField('guide_version')
    tags = serializers.SerializerMethodField('tag_list')
    versions = DownloadSerializer(many=True, read_only=True)

    class Meta:
        model = Guide
        fields = ('name', 'file', 'date', 'num_version', 'tags', 'versions')

    def latest_guide_date(self, guide):
        try:
            return guide.latest_version.date
        except:
            return None

    def guide_version(self, guide):
        try:
            return guide.latest_version.num_version
        except:
            return None

    def tag_list(self, guide):
        try:
            return ','.join([t.name for t in guide.tags.all()])
        except:
            return None

    def guide_file(self, guide):
        try:
            return self.context['request'].build_absolute_uri(guide.latest_version.file.url)  # noqa
        except:
            return ''
