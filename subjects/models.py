from django.db import models

# Create your models here.
class subject(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=5)
    status = models.CharField(max_length=2) 
    DisplayFields = ("id","name","code","status")
    SearchableFields = ["name","code"]
    FilterFields = ["name"]