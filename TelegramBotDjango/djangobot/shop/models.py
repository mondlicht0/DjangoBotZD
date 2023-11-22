from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()

class Video(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)