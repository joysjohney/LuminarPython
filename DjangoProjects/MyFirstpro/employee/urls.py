from django.shortcuts import render
from django.urls import path,include
from employee.views import reg,empReg,login


urlpatterns = [
    path("reg/",reg,name="reg"),
    path("sign/",empReg,name="signUp"),
    path("login/",lambda request:render(request,"login.html"),name="login"),
    path("login/",login,name="login")



]
