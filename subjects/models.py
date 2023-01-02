from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=250)
    status = models.CharField(max_length=230)