from django.db import models

# Create your models here.


class Province(models.Model):
    name = models.CharField(max_length=30)


class City(models.Model):
    name = models.CharField(max_length=30)
    postcode = models.CharField(max_length=6)
    area_code = models.CharField(max_length=4)
    longitude = models.FloatField(max_length=20)
    latitude = models.FloatField(max_length=20)
    province = models.OneToOneField(Province)


class District(models.Model):
    name = models.CharField(max_length=30)
    city = models.OneToOneField(City)