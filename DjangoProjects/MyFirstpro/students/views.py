from django.shortcuts import render, redirect
from students.models import students

# Create your views here.
def reg(request):
    return render(request,"reg.html")

def stuReg(request):
    name=request.POST.get("first")
    email=request.POST.get("email")
    uname=request.POST.get("uname")
    password=request.POST.get("password")
    course=request.POST.get("course")
    obj=students(name=name,email=email,uname=uname,password=password,course=course)
    obj.save()
    print("object saved")
    return render(request,"login.html")


def login(request):
    email=request.POST.get("email")
    password=request.POST.get("pwd")
    try:
        student=students.objects.get(email=email)
        if(student):
            pswrd=students.pwd
            if(password==pswrd):
                print("login success")
                return render(request,"home.html")
            else:
                return redirect("login")
    except:
        return redirect("login")

def stuhome(request):
    queryset=students.objects.all()
    context={}
    context["students"]=queryset
    return render(request,"home.html")
