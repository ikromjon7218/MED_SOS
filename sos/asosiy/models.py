from django.db import models

class Inson(models.Model):
    ism = models.CharField(max_length=30)
    tugilgan_yil = models.DateField()
    vaqt = models.DateTimeField(auto_now_add=True)
    tel_raqam = models.PositiveIntegerField()
    faol = models.BooleanField(default=True)
    longlitude = models.CharField(max_length=20)
    latitude = models.CharField(max_length=20)
    geolocation_url = models.CharField(max_length=60, blank=True)