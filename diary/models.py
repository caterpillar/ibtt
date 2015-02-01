from django.db import models
from baby.models import Baby

# Create your models here.


class PictureDiary(models.Model):
    input_time = models.DateTimeField(auto_now=True)
    diary_time = models.DateTimeField(auto_now=True)
    baby = models.ForeignKey(Baby)


class Picture(models.Model):
    key = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    picture_diary = models.ForeignKey(PictureDiary)

