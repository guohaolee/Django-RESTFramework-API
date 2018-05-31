from django.db import models

# Create your models here.

class nz_data(models.Model):
	id = models.BigAutoField
	wmo = models.IntegerField(blank=True,null=True)
	chom = models.IntegerField(blank=True,null=True)
	names = models.CharField(max_length=100,blank=True)
	heights = models.FloatField(blank=True, null=True) 
	types = models.CharField(max_length=100, blank=True)
	cloud_base_m = models.CharField(max_length=100,blank=True)
	
	def __str__(self):
		return self.names

	class Meta:
                verbose_name = "NZ_table"


class queensland_weather(models.Model):
	id=models.BigAutoField
	wmo_id=models.BigIntegerField(blank=True,null=True)
	bom_id=models.BigIntegerField(blank=True,null=True)
	tz=models.CharField(max_length=100,blank=True,null=True)
	station_name=models.CharField(max_length=100,blank=True,null=True)
	station_height=models.FloatField(blank=True,null=True)
	station_type=models.CharField(max_length=100,blank=True,null=True)
	latitude=models.DecimalField(max_digits=100, decimal_places=2,blank=True,null=True)
	longitude=models.DecimalField(max_digits=100, decimal_places=2,blank=True,null=True)
	state=models.CharField(max_length=100,blank=True,null=True)
	forecast_district_id=models.CharField(max_length=100,blank=True,null=True)
	description=models.CharField(max_length=256,blank=True,null=True)
	period_index=models.BigIntegerField(blank=True,null=True)
	time_utc=models.CharField(max_length=100,blank=True,null=True)
	time_local=models.CharField(max_length=100,blank=True,null=True)
	wind_src=models.CharField(max_length=100,blank=True,null=True)
	level_index=models.IntegerField(blank=True,null=True)
	level_type=models.CharField(max_length=100,blank=True,null=True)
	apparent_temp=models.FloatField(blank=True,null=True)
	cloud=models.CharField(max_length=100,blank=True,null=True)
	cloud_base_m=models.IntegerField(blank=True,null=True)
	cloud_oktas=models.IntegerField(blank=True,null=True)
	cloud_type_id=models.IntegerField(blank=True,null=True)
	cloud_type=models.CharField(max_length=100,blank=True,null=True)
	delta_t=models.FloatField(blank=True,null=True)
	gust_kmh=models.IntegerField(blank=True,null=True)
	wind_gust_spd=models.IntegerField(blank=True,null=True)
	air_temperature=models.FloatField(blank=True,null=True)
	dew_point=models.FloatField(blank=True,null=True)
	pres=models.FloatField(blank=True,null=True)
	msl_pres=models.FloatField(blank=True,null=True)
	qnh_pres=models.FloatField(blank=True,null=True)
	rain_hour=models.FloatField(blank=True,null=True)
	swell_dir=models.CharField(max_length=100,blank=True,null=True)
	swell_height=models.FloatField(blank=True,null=True)
	swell_period=models.IntegerField(blank=True,null=True)
	rain_ten=models.FloatField(blank=True,null=True)
	rel_humidity=models.IntegerField(blank=True,null=True)
	sea_height=models.CharField(max_length=100,blank=True,null=True)
	vis_km=models.FloatField(blank=True,null=True)
	weather=models.CharField(max_length=100,blank=True,null=True)
	wind_dir=models.CharField(max_length=100,blank=True,null=True)
	wind_dir_deg=models.IntegerField(blank=True,null=True)
	wind_spd_kmh=models.IntegerField(blank=True,null=True)
	wind_spd=models.IntegerField(blank=True,null=True)
	rainfall=models.FloatField(blank=True,null=True)
	rainfall_24hr=models.FloatField(blank=True,null=True)
	maximum_air_temperature=models.FloatField(blank=True,null=True)
	minimum_air_temperature=models.FloatField(blank=True,null=True)
	maximum_gust_spd=models.IntegerField(blank=True,null=True)
	maximum_gust_kmh=models.IntegerField(blank=True,null=True)
	maximum_gust_dir=models.CharField(max_length=100,blank=True,null=True)

	def __str__(self):
		return self.station_name

	class Meta:
		verbose_name = "queensland_weather_table"

