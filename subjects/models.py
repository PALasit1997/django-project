from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=5)
    status = models.CharField(max_length=2) 