from email.policy import default
from enum import auto
from tabnanny import verbose
from tkinter import CASCADE
from types import NoneType
from django.db import models
from django.contrib.auth.models import AbstractUser 
# Create your models here.

class User(AbstractUser):
    pass

class Client(models.Model):

    first_name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20)
    order_name = models.CharField(max_length=20)
    total = models.IntegerField(default=0)
    phone_number = models.CharField(max_length=16)
    comment = models.CharField(max_length=500)
    image = models.ImageField()
    seamstress = models.ForeignKey("Seamstress", on_delete=models.CASCADE)   
    def __str__(self):
        return self.first_name + ' ' + self.second_name
class Seamstress(models.Model):
    class Meta:
        verbose_name = "Seamstress"
        verbose_name_plural = "Seamstresses"

    name = models.CharField(max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

