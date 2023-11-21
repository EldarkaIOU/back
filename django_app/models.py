from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    category = models.CharField(max_length=255)
    release = models.IntegerField()

