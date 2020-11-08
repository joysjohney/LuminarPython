from django.shortcuts import render


# Create your views here.
def calc(request):
    return render(request, "CalculationPage.html")


def add(request):
    no1 = int(request.POST.get("no1"))
    no2 = int(request.POST.get("no2"))
    res = no1 + no2
    return render(request, "CalculationPage.html", {"res":res})

def sub(request):
    no3 = int(request.POST.get("no3"))
    no4 = int(request.POST.get("no4"))
    res = no3 + no4
    return render(request, "CalculationPage.html", {"res":res})

