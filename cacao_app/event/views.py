# -*- coding: utf-8 -*-
from datetime import datetime
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import EventsSerializer
from .models import Event, CountryEvent


@api_view(['GET'])
def events_collection(request):
    if request.method == 'GET':
        events = Event.objects.filter(start__gte=datetime.now())
        serializer = EventsSerializer(events, many=True, context={"request": request})  # NOQA
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def events_per_country(request, country_code):

    try:
        ev = Event.objects.filter(
            start__gte=datetime.now(),
            events_country__country=country_code
        )
    except Event.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = EventsSerializer(ev, many=True, context={"request": request})  # NOQA
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
