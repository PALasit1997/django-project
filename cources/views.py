from django.shortcuts import render
from django.http import HttpResponse,HttpResponse
# from students.models import Students

# Create your views here.


def cources_name(request):

    
    return render(request,"index.html")