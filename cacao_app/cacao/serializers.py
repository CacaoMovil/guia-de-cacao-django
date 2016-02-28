# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Guide, Download


class GuidesSerializer(serializers.ModelSerializer):
    """ Serializers for list all guides"""
    date = serializers.SerializerMethodField('latest_guide_date')
    file = serializers.SerializerMethodField('guide_file')
    num_version = serializers.SerializerMethodField('guide_version')

    class Meta:
        model = Guide
        fields = ('name', 'file', 'date', 'num_version')

    def latest_guide_date(self, guide):
        return guide.latest_version.date

    def guide_version(self, guide):
        return guide.latest_version.num_version

    def guide_file(self, guide):
        return guide.latest_version.file.url


class GuideSerializer(serializers.ModelSerializer):
    """Serializers for guide element, guide versions and last guide"""
    
    class Meta:
        model = Download
        fields = ('name', 'file', 'date', 'num_version')