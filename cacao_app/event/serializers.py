# -*- coding: utf-8 -*-

from rest_framework import serializers
from django_countries.serializer_fields import CountryField

from .models import Event, CountryEvent


class CountryEventSerializer(serializers.ModelSerializer):
    code = serializers.ReadOnlyField(source='country.code')
    name = serializers.SerializerMethodField()

    class Meta:
        model = CountryEvent
        fields = ('code', 'name')

    def get_name(self, obj):
        return obj.country.name


class EventsSerializer(serializers.ModelSerializer):
    events_country = CountryEventSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = (
            'name', 'description', 'start', 'end', 'events_country'
        )
