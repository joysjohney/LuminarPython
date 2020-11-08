
from django.contrib import admin
from django.urls import path
from mathsapp.views import calc,add,sub

urlpatterns = [
    path('calc/', calc, name="calc"),
    path('sub/', sub, name="sub"),
    path('add/', add, name="add"),



]

