from django.contrib import admin
# from django.contrib.admin.sites import site
# from students.models import Students
from .models import Students


class StudentsAdmin(admin.ModelAdmin):
    list_Display = ('name','address','gender','email','password','image','status')

    @admin.display(empty_value='name')
    def name(self, obj):
        return obj.name
admin.site.register(Students)
# Register your models here.
