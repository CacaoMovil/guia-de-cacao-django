# -*- coding: utf-8 -*-

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import EventsSerializer
from .models import Event


@api_view(['GET'])
def events_collection(request):
    if request.method == 'GET':
        events = Event.objects.all()
        serializer = EventsSerializer(events, many=True, context={"request": request})  # NOQA
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def events_per_country(request, country_code):
    try:
        download = Download.objects.get(guide=number, num_version=num_version)
    except Download.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = DownloadSerializer(download, context={"request": request})
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
