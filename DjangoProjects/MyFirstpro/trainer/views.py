from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse


def treg(request):

    return render(request,"trainerreg.html")

def tlog(request):
    return render(request,"trainerlogin.html")