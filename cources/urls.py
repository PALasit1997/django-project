# from django.contrib import admin
from django.urls import path
from cources import views


urlpatterns = [

    path("create-cources/",views.cources_name),
]