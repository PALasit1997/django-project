from django.shortcuts import render , redirect
from django.http import HttpResponse,HttpResponseRedirect
from students.models import Students
from .forms import signup,login_form
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
# from django.contrib.auth.forms import UserCreationForm
# from .forms import user_form
import math


def home(request):
    return render(request,"index.html")
    # return HttpResponse("test home page")

def singup(request):
    # data=""
    # fn=user_form()
    if request.method=="POST":
        form = signup(request.POST)
        if form.is_valid():
            form.save()
            return redirect(login)
            # return HttpResponse("<h1>signup page successfully</h1>")
    else:
        form = signup()
    data = {
        # "froms":fn,
            "form":form
    }

        # username = request.POST.get("username")
        # s1=request.POST.get("name")
        # s2=request.POST.get("email")
        # s3=request.POST.get("password")
        # # print(username,s1,s2,s3)
        # my_user=Students.objects.create_user(username,s1,s2,s3)
        # my_user.save()
        # return HttpResponse("this page is sucessfully passed")
    return render(request,"signup.html",data)


def login(request):
    if request.method=="POST":
        form = login_form(request.POST)
        # print(form)

        if form.is_valid():
            cd=form.cleaned_data
            user = authenticate(request,username=cd["username"],password=cd["password"])
            if user is not None:
                if user.is_active:
                    login_form(request,user)
                    # if request.GET.get('Next'):
                    #     return HttpResponseRedirect(request.GET['next'])
                    # return HttpResponse("login successfully")
                    return redirect("home")
                        #--: which call redirect page in (url / function name / name?) ?
                else:
                    return HttpResponse("disable account")

            else:
                return HttpResponse("invalid login")
    else:
        form=login_form()

    #     x = request.POST['username']
    #     y = request.POST['password']
    #     print("asit pal is a good boy")
    #     # print(username1)
    #     # print(password)
    # data={
    #     "username":x,
    #     "password":y,
    # }

        # x=request.POST.get("username")
        # y=request.POST.get("password")
        # # print(x)
        # stu=Students.objects.filter(email=x,password=y).first()
        # if stu.email== x:
    #     # if  x in stu:
    #     for x in stu:
            # return render(request,"signup.html")
            # return redirect(create_user)
    #     # for student in stu:
    #     print(x.name)
    #     # print(stu.email)
    # #   print("welcome to india")
    return render(request,"login.html",{"form":form})

# @login_required
def log_out(request):
    logout(request)
    return render(request,"loginpage.html")
    # return HttpResponse("logout page is successfully")
    # return render(request,"calculator.html")

@login_required(login_url="/login/")
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


def studentDetails(request,id):
    # if request.method=="POST":
    #     x=request.POST.get("username")
    #     y=request.POST.get("password")
    #     print(x)
    #     print(y)
    #     stu=Students.objects.filter(email=x,password=y).first()
    #     print(stu)


    students = Students.objects.get(id=id)
    # students = Students.objects.all().values('name')
    # students = Students.objects.filter(name='gmail').values()
    print(students)
    students.show()
    # print(students.name)
    # for student in students:
    #     student.save()
    #     print(student.name)
        # pass

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
            s7=int(request.POST.get("phone_no"))
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


def delete_student(request,emp_id):
    students = Students.objects.get(id=emp_id)
    students.delete()
    # print("hello world")
    print(emp_id)
    # return students
    return render(request,'index.html',{}) 

def update_student(request,stu_id):
    students = Students.objects.get(id=stu_id)

    print(stu_id)
    # return students
    return render(request,'update_student.html',{"students":students})  

def do_update_student(request,stu_id):
    if request.method =="POST":
        s1=str(request.POST.get("name"))
        s2=str(request.POST.get("email"))
        s3=str(request.POST.get("password"))
        s4=(request.POST.get("gender"))
        s5=(request.POST.get("image"))
        s6=str(request.POST.get("address"))
        s7=str(request.POST.get("phone_no"))
        s8=str(request.POST.get("status"))   

        students = Students.objects.get(id=stu_id)
        print(students.name)
        students.name=s1,
        students.email = s2,             
        students.password = s3,
        students.gender = s4, 
        students.image = s5,
        students.address = s6,
        students.phone_no = s7,           
        students.status = s8,
        students.save()

    return redirect("/signup/")  

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

    
# @login_required
def loginPage(request):
    print("asit")
   
    return render(request,"loginpage.html")

    #   return HttpResponse("Hello, world. You're at the polls index.")



def create(request):
    return HttpResponse("welcome to india")

def allcoures(request,courseId):
    return HttpResponse(courseId)

    