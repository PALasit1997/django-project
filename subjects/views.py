from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponse
from subjects.models import subject

# Create your views here.

def subject_name(request):
    data=""
    
    # print("asit pal")
    if request.method=="POST":
        s=request.POST.get("subject")
        c=request.POST.get("code")
        s1=request.POST.get("status")
        data={
            "subject":s,
            "code":c,
            "status":s1
            }
        print(data)
        obj = subject(
            name=request.POST.get("subject"),
            code = request.POST.get("code"),             
            status = request.POST.get("status"),
            ).save()
        print(obj)    
    return render(request,"subjectDetails.html",{"data":data})
    # return HttpResponse("i am asit pal")


def subject_details(request):
    try:
        # print("asit pal")
        subjects=subject.objects.all()
        # print(subjects)
    except:
        print("check detatis this page....")
    # messages.success(request,"this page is successfully.....")
    return render(request,"subject_table.html",{"subject":subjects})

def EditSubject(request,subjectId):
    sub=subject.objects.get(id=subjectId)
    subject1={"subject":sub}
    return render(request,"Editsub.html",subject1)

def delete_sub(request,subjectId):
    delete=subject.objects.get(id=subjectId)
    delete.delete()
    print("i am asit pal")
    return redirect('/subject_details')
    # return render(request,delete_sub.html)