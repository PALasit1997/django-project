from django.urls import path
from subjects import views

urlpatterns = [
    path("create-subjects/",views.subject_name),
    path("get-subjects/",views.subject_details),
    path("edit-subjects/<subjectId>",views.EditSubject,name="edit_sub"),
    path("delete-sub/<subjectId>",views.delete_sub,name="delete_sub"),
]