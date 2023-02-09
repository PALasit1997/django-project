from django.contrib import admin
from .models import subject

# Register your models here.

# admin.site.register(subject)

@admin.register(subject)
class subjectadmin(admin.ModelAdmin):
    list_display = subject.DisplayFields
    search_fields = subject.SearchableFields
    list_filter = subject.FilterFields