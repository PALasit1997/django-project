from django.contrib import admin
# from django.contrib.admin.sites import site
# from students.models import Students
from .models import Students


@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display =Students.DisplayFields
    search_fields = Students.SearchableFields
    list_filter = Students.FilterFields
    # @admin.display(empty_value='name')
    # def name(self, obj):
    #     return obj.name
# admin.site.register(Students)
# Register your models here.
