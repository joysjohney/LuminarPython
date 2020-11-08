
from django.contrib import admin
from django.urls import path
from trainer.views import treg,tlog

urlpatterns = [
    path('treg/', treg),
    path('tlog/', tlog),
]
