from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=100).primary_key
    avatar = models.CharField(max_length=1000)
    language = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    url = models.CharField(max_length=1000)
