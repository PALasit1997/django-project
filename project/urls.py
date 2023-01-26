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
from django.urls import path,include
from project import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("cources.urls")),
    path('', include("subjects.urls")),
    path('', include('product.urls')),


    # path('', views.home),
    path('signup/', views.singup),
    path('signin/', views.singin),
    # path('signout/', views.singout,name=singout),



    path('', views.loginPage),
    path('create-user/', views.aboutUs),
    path('get-student/', views.studentDetails),
    path('user-data/', views.user_data),
    path('edit-student/<student>',views.edit_student,name="edit-student"),
    path('create-student/', views.aboutUs),
    path('calculator/', views.calculator),
    path('even-odd/', views.evenOdd),
    path('solvedevenOdd/', views.solvedevenOdd),
    path('markshit/', views.markshit),
    path('homepage/', views.homePage),
    # path('get-student/', views.getStudent),
    path('create/', views.create),
    path('all-course/<str:courseId>', views.allcoures),
]
