#views are not used as we are using viewset

from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import generics

from . import models
from . import serializers

def index(request):
    return HttpResponse("Hello World")

class Queensland_WeatherView(generics.ListCreateAPIView):
    queryset = models.queensland_weather.objects.all()
    serializer_class = serializers.queensland_weather_serializer

class nzView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.nz_data.objects.all()
    serializer_class = serializers.nz_serializer
