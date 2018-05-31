from rest_framework import serializers
from . import models

"""Serializer for queensland_weather"""
class queensland_weather_serializer(serializers.ModelSerializer):

  class Meta:
    model = models.queensland_weather
    fields = '__all__'

"""Serializer for nz"""
class nz_serializer(serializers.ModelSerializer):

  class Meta:
    model = models.nz_data
    fields = (
		'id',
		'names',
		'heights',
		'types',
		)

