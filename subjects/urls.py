from django.urls import path
from subjects import views

urlpatterns = [
    path("create-subjects/",views.subject_name),
    path("get-subjects/",views.subject_details),
]