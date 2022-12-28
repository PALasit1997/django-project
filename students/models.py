from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    gender = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=30)
    image = models.CharField(max_length=150)
    status = models.CharField(max_length=30)
