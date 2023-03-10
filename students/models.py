from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    image = models.CharField(max_length=150)
    address = models.CharField(max_length=250)
    phone_no = models.CharField(max_length=10)
    status = models.CharField(max_length=30)
    DisplayFields = ['id','name','email','password','gender','image','address','phone_no','status']
    SearchableFields = ['id','name','phone_no']
    FilterFields = ['name']