from django.db import models

# Create your models here.
from django.db.models import CharField


class employee(models.Model):
    name=models.CharField(max_length=120)
    email=models.CharField(max_length=120,unique=True)
    uname=models.CharField(max_length=125,unique=True)
    password=models.CharField(max_length=120)
    salary=models.IntegerField(default=5000)

    def __str__(self):
        return self.name