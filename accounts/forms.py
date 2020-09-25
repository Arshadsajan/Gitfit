from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Clients

class CreateUserForm(UserCreationForm):
    class Meta:
         model=User
         fields=['username','email','password1','password2']

class ClientsForm(ModelForm):
    class Meta:
        model=Clients
        #fields=['name','email','adress','gender','age','weight','height','contact_no']
        fields='__all__'
