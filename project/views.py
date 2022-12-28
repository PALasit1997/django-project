from django.shortcuts import render
from django.http import HttpResponse,HttpResponse
# from students.models import Students
# from.forms import user_form
import math


def markshit(request):
    data=""
    if request.method=="POST":
        s1=eval(request.POST.get("Ben"))
        s2=eval(request.POST.get("Eng"))
        s3=eval(request.POST.get("Math"))
        s4=eval(request.POST.get("Hist"))
        s5=eval(request.POST.get("Geo"))
        t=s1+s2+s3+s4+s5
        p=t*100/500
        x = math.ceil(p)
        if p>80:
            d="first devition"
        elif p>60:
            d="decond devition"
        elif p>45:
            d="third devition"
        elif d>0:
            d="fail"
        # print(p)
        # print(t)
        data={
            "total":t,
            "persentagae":x,
            "Divition":d
        }
        return render(request,"markshit.html",data)
    return render(request,"markshit.html")


def evenOdd(request):
    res=""
    if request.method=="POST":
        res1=eval(request.POST.get("first"))
        if res1%2==0:
            res="even number"
        else :
            res="odd number"
        print(res1)
    return render(request,"evenOdd.html",{"res":res})

def calculator(request):
    res=""
    try:
        if request.method=="POST":
            n1=eval(request.POST.get("first"))
            n2=eval(request.POST.get("second"))
            opr=request.POST.get("opr")
            if (opr=="+"):
                res=n1+n2
            elif (opr=="-"):
                res=n1-n2
            elif (opr=="*"):
                res=n1*n2
            elif (opr=="/"):
                res=n1/n2
    except :
        res="invalid opreator"
    
    return render(request,"calculator.html",{"res":res})

def homePage(request):
    data={
        "name" : "home Page 1  ",
        "roll"  : 11,
        "course" :["php","java","html"],
        "number":[],
        "studentData":[
            {"name":"asit pal","roll_no":10},
            {"name":"biswajit pal","roll_no":1}
        ]
    }
    
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request,"index.html",data)

    

def index(request):
    return render(request,"basic-table.html")

    #   return HttpResponse("Hello, world. You're at the polls index.")

  
def aboutUs(request):
    print(request.POST)
    return render(request,"forms/userDetails.html")

    # return HttpResponse("asit pal")

def create(request):
    return HttpResponse("welcome to india")

def allcoures(request,courseId):
    return HttpResponse(courseId)