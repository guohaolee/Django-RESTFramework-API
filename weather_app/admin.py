from django.contrib import admin
from .models import queensland_weather
from .models import nz_data

from import_export.admin import ImportExportModelAdmin
from django.contrib import admin

# Register your models here.

#admin.site.register(queensland_weather)
#admin.site.register(nz_data)

@admin.register(queensland_weather)
class queensland_weather_Admin(ImportExportModelAdmin):
    pass

@admin.register(nz_data)
class nz_data_Admin(ImportExportModelAdmin):
    pass

