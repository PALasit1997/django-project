"""project URL Configuration


The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from project import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('get-student/', views.getStudent),
    path('create-user/', views.aboutUs),
    path('homepage/', views.homePage),
    path('about/', views.aboutUs),
    path('create/', views.create),
    path('all-course/<str:courseId>', views.allcoures),
    path('calculator/', views.calculator),
    path('even-odd/', views.evenOdd),
    path('markshit/', views.markshit),
    path('student-dtls/', views.student_Dtls),
    path('user-data/', views.user_data),
]
