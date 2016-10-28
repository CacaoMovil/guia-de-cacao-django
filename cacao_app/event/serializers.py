# -*- coding: utf-8 -*-

from rest_framework import serializers
from django_countries.serializer_fields import CountryField

from .models import Event


class EventsSerializer(serializers.ModelSerializer):
    country_code = serializers.ReadOnlyField(source='country.code')
    country_name = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = (
            'name', 'description', 'start',
            'end', 'country_code', 'country_name'
        )

    def get_country_name(self, obj):
        return obj.country.name
