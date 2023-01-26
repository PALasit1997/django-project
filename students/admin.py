from django.contrib import admin
# from django.contrib.admin.sites import site
# from students.models import Students
from .models import Students


# class StudentsAdmin(admin.ModelAdmin):
#     list_Display("name","address","gender","email","password","image","status")
admin.site.register(Students)
# Register your models here.
