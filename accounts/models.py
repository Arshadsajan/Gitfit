from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.
""" class GymTrainer(models.Model):
    name=name=models.CharField(max_length=30,null='true')
    email=models.EmailField(null=True)
    contact_no=models.CharField(max_length=10)
    def __str__(self):
        return self.name
 """
class Clients(models.Model):
    Gender=(('male','Male'),('female','Female'),('others','Others'))
    name=models.CharField(max_length=30,null='true')
    email=models.EmailField(null=True,blank=True,unique=True)
    adress=models.TextField()
    gender=models.CharField(max_length=6,choices=Gender)
    age=models.IntegerField()
    weight=models.FloatField()
    height=models.FloatField()
    contact_no=models.CharField(max_length=10)
    gymUser=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)

    def __str__(self):
        return self.name