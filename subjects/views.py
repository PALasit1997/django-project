from django.shortcuts import render
from django.http import HttpResponse,HttpResponse
from subjects.models import subject

# Create your views here.

def subject_name(request):
    data=""
    try:
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
    except:
        print("pleace fill the subject from....")
    
    
    return render(request,"subjectDetails.html",{"data":data})
    # return HttpResponse("i am asit pal")


def subject_details(request):
    try:
        # print("asit pal")
        subjects=subject.objects.all()
        # print(subjects)
    except:
        print("check detatis this page....")

    return render(request,"subject_table.html",{"subject":subjects})