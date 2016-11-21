from django.db import models


class weather_observation (models.Model):
    observation = models.CharField(max_length=140)
    observationTime = models.DateTimeField()
    stationName = models.CharField(max_length=140)
    icao = models.CharField(max_length=40)
    countryCode = models.CharField(max_length=10)
    elevation = models.IntegerField()
    dewPoint = models.IntegerField()
    humidity = models.IntegerField()
    cloudsCode = models.CharField(max_length=60)
    weatherCondition = models.CharField(max_length=15)
    hectoPascAltimeter = models.DecimalField(max_digits=5,
        decimal_places=1, default=0)
    windDirection = models.DecimalField(max_digits=5,
        decimal_places=1, default=0)
    windSpeed = models.IntegerField()
    temperature = models.IntegerField()
    lat = models.DecimalField('Coordenadas UTM-E', max_digits=17,
        decimal_places=14, null=False, blank=True, default=0)
    lng = models.DecimalField('Coordenadas UTM-E', max_digits=17,
        decimal_places=14, null=False, blank=True, default=0)

    def __str__(self):
        return self.observation