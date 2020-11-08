from django.shortcuts import render
from employee.models import employee

# Create your views here.
def reg(request):
    return render(request,"empreg.html")

def empReg(request):
    name=request.POST.get("first")
    email=request.POST.get("email")
    uname=request.POST.get("uname")
    password=request.POST.get("password")
    salary=request.POST.get("salary")
    obj=employee(name=name,email=email,uname=uname,password=password,salary=salary)
    obj.save()
    print("object saved")
    return render(request,"login.html")


def login(request):
    email=request.POST.get("email")
    password=request.POST.get("pwd")
    try:
        employee=employee.objects.get(email=email)
        if(employee):
            pswrd=employee.pwd
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