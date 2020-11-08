from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db.models import CharField


class student(models.Model):
    name=models.CharField(max_length=120)
    email=models.CharField(max_length=120,unique=True)
    uname=models.CharField(max_length=125,unique=True)
    password=models.CharField(max_length=120)
    course=models.CharField(max_length=120)

    def __str__(self):
        return self.name