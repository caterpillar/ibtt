from django.db import models
from django.contrib.auth.models import User
from base.models import Province, City, District

# Create your models here.


class Parents(models.Model):
    user = models.OneToOneField(User)
    mobile = models.CharField(max_length=13)
    sex = models.CharField(max_length=10)
    birthday = models.DateTimeField(blank=True, null=True)
    province = models.ForeignKey(Province, blank=True, null=True)
    city = models.ForeignKey(City, blank=True, null=True)
    district = models.ForeignKey(District, blank=True, null=True)
    settings = models.OneToOneField('Settings')


class Baby(models.Model):
    nickname = models.CharField(max_length=50)
    sex = models.CharField(max_length=10)
    birthday = models.DateTimeField(auto_now=True)
    parents = models.ForeignKey(Parents)


class Settings(models.Model):
    diary_frequency = models.CharField(max_length=10)