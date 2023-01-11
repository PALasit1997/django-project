from django.shortcuts import render
from django.http import HttpResponse,HttpResponse

# Create your views here.

def subject_name(request):
    
    # return HttpResponse("i am asit pal")
    return render(request,"login.html")

def subject_details(request):

    return render(request,"")