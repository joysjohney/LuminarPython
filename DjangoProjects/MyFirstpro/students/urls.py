
from django.contrib import admin
from django.shortcuts import render
from django.urls import path,include
from students.views import reg,stuReg,login


urlpatterns = [
    path("reg/",reg,name="reg"),
    path("sign/",stuReg,name="signUp"),
    path("login/",lambda request:render(request,"login.html"),name="login"),
    path("login/",login,name="login")

]
