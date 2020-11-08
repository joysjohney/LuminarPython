from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def studreg(request):

    return render(request,"studentreg.html")

def studlog(request):
    return render(request,"studentlogin.html")

def regDetails(request):
    email=request.POST.get("email")
    password=request.POST.get("pwd")
    print("email=",email,"password=",password)
    return render(request, "studentreg.html")

def loginDetails(request):
    email = request.POST.get("uname")
    password = request.POST.get("pwrd")
    print("email=", email, "password=", password)
    return render(request,"studentlogin.html")

