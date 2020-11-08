
from django.contrib import admin
from django.urls import path
from student.views import studreg,studlog,regDetails,loginDetails

urlpatterns = [
    path('studreg/', studreg, name="studreg"),
    path('studlog/', studlog, name="studlog"),
    path('GetReg/', regDetails, name="getRegDetails"),
    path('Getlog/', loginDetails, name="loginDetails"),
]
