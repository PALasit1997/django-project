from django.shortcuts import render , redirect
from django.http import HttpResponse,HttpResponse
from students.models import Students
# from django.contrib.auth.models import Students
# from.forms import user_form
import math


def home(request):
    return render(request,"index.html")
    # return HttpResponse("test home page")

def singup(request):
    data=""

    if request.method=="POST":
        username = request.POST.get("username")
        s1=request.POST.get("name")
        s2=request.POST.get("email")
        s3=request.POST.get("password")
        # print(username,s1,s2,s3)
        my_user=Students.objects.create_user(username,s1,s2,s3)
        my_user.save()
        return HttpResponse("this page is sucessfully passed")
    return render(request,"signup.html",{"data":data})


def singin(request):
    if request.method=="POST":

        x=request.POST.get("username")
        y=request.POST.get("password")
        # print(x)
        stu=Students.objects.filter(email=x,password=y).first()
        # if stu.email== x:
        # if  x in stu:
        # if x in stu:
        for x in stu:
            return render(request,"signup.html")
        # for student in stu:
        print(x.name)
        # print(stu.email)
    #   print("welcome to india")
    return render(request,"signin.html")


# def singout(request):
#     return render(request,signout.html)

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

def solvedevenOdd(request):
    res=""
    if request.method=="POST":
        if request.POST.get("first")=="":
            return render(request,"evenOdd.html",{"error":True})
        
        res1=eval(request.POST.get("first"))
        if res1%2==0:
            res="even number"
        else :
            res="odd number"
        print(res1)
    return render(request,"evenOdd.html",{"res":res})

def calculator(request):
    data={ }
    # res=""
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
            data = {
                "n1" : n1,
                "n2" : n2,
                "res": res
            }
    except :
        res="invalid opreator"
    print(data)
    return render(request,"calculator.html",data)


def studentDetails(request):

    students = Students.objects.all()
    print(students)
    for student in students:
        print(student.name)

    return render(request,"studentDetails.html",{"students":students})


def user_data(request):

    students=Students.objects.all()

    return render(request,"forms/basic-table.html",{"students":students})


def aboutUs(request):
    data=""
    try:
        if request.method=="POST":
            
            s1=str(request.POST.get("name"))
            s2=str(request.POST.get("email"))
            s3=str(request.POST.get("password"))
            s4=(request.POST.get("gender"))
            s5=(request.POST.get("image"))
            s6=str(request.POST.get("address"))
            s7=str(request.POST.get("phone_no"))
            s8=str(request.POST.get("status"))
            data={
                "name":s1,
                "email":s2,
                "password":s3,
                "gender":s4,
                "image":s5,
                "address":s6,
                "phone_no":s7,
                "status":s8,
            }
            # print(data)
        obj = Students(
                        # id=16,
                        name=s1,
                        email = s2,             
                        password = s3,
                        gender = s4, 
                        image = s5,
                        address = s6,
                        phone_no = s7,           
                        status = s8,
            ).save()
        # print(obj)
    except:
        print("invalid opr......")
    # print(request.POST)
    return render(request,"forms/userDetails.html",{"data":data})

def edit_student(request,student):
    students = student.objects(id=student)
    # print("hello world")
    print(students)
    # return students
    return render(request,'index.html',{"student":students})

def getStudent(request):
    students = Students.objects.all()
    data = {
        'students': students
    }
    return render(request,'index.html')

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
    return render(request,"homepage.html",data)

    

def loginPage(request):
    print("asit")
   
    return render(request,"login.html")

    #   return HttpResponse("Hello, world. You're at the polls index.")



def create(request):
    return HttpResponse("welcome to india")

def allcoures(request,courseId):
    return HttpResponse(courseId)

    