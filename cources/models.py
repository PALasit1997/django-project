from django.db import models

# Create your models here.


class cources(models.Model):
    student_id=models.CharField(max_length=250) 
    subject_id=models.CharField(max_length=250) 
    status=models.CharField(max_length=250) 