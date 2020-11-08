from django.shortcuts import render, redirect
from Books.forms import *


# Create your views here.

def create(request):
    template_name = "create.html"
    form = BookForm()
    dict = {}
    dict["form"] = form
    query = Book.objects.all()
    dict["books"] = query
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            query = Book.objects.all()
            dict["books"] = query
            return render(request, template_name, dict)
        else:
            dict["form"] = form
    return render(request, template_name, dict)


def view(request, pk):
    obj = Book.objects.get(id=pk)
    dict={}
    dict["items"] = obj
    return render(request, "view.html", dict)


def update(request, pk):
    query = Book.objects.get(id=pk)
    form = Bookupdateform(instance=query)
    dict={}
    dict["form"] = form
    if request.method == "POST":
        form = Bookupdateform(instance=query, data=request.POST)
        form.save()
        return redirect("create")

    return render(request, "update.html", dict)


def delete(request, pk):
    obj = Book.objects.get(id=pk).delete()
    return redirect("create")


