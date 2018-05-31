from rest_framework import viewsets

from . import models
from . import serializers


class Queensland_WeatherView(viewsets.ModelViewSet):

#	This viewset automatically provides `list`, `create`, `retrieve`,
#	`update` and `destroy` actions.

#	Additionally we also provide an extra `highlight` action.

    
	queryset = models.queensland_weather.objects.all()
	serializer_class = serializers.queensland_weather_serializer
#	permission_classes = [IsAccountAdminOrReadOnly]
    
#    	def get_queryset(self):
#        return self.request.user.accounts.all()

# permission class refer to this documentation:
#http://www.django-rest-framework.org/api-guide/permissions/


class nzView(viewsets.ReadOnlyModelViewSet):

#    A simple ViewSet for viewing accounts.
    
	queryset = models.nz_data.objects.all()
	serializer_class = serializers.nz_serializer
