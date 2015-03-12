# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Guide, Download

class DownloadSerializer(serializers.ModelSerializer):
    """
    Serializers for guide element, guide versions
    and last guide
    """
    class Meta:
        model = Download
        fields = ('name', 'file', 'date', 'num_version')

class GuidesSerializer(serializers.ModelSerializer):
    """
    Serializers for list all guides
    """
    date = serializers.SerializerMethodField('latest_guide_date')
    file = serializers.SerializerMethodField('guide_file')
    num_version = serializers.SerializerMethodField('guide_version')
    versions = DownloadSerializer(many=True, read_only=True)

    class Meta:
        model = Guide
        fields = ('name', 'file', 'date', 'num_version', 'versions')

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

    def guide_file(self, guide):
        try:
            return guide.latest_version.file.url
        except:
            return ''
