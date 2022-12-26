from django.shortcuts import render
from django.http import HttpResponse,HttpResponse

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