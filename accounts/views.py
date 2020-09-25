from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.contrib.auth.models import User
from .models import Clients
from .forms import CreateUserForm,ClientsForm

@login_required(login_url='login')
def home(request):
    # user1=User.objects.get(id=request.user.id)
    # all_clients=user1.clients_set.all()
    # context={'clients':all_clients}
    x=request.user.clients_set.all()
    context={'clients':x}

    return render(request,'accounts/home.html',context)

def RegisterPage(request):
    if request.user.is_authenticated:
        return redirect("home")

    else:
        form=CreateUserForm()

        if request.method=='POST':
            form=CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user=form.cleaned_data.get('username')
                messages.success(request,'Account created for '+ user)
                return redirect('login')

        context={'form':form}
        return render(request,'accounts/register.html',context)

def LoginPage(request):
    if request.user.is_authenticated:
        return redirect("home")

    else:
        if request.method=='POST':
            username=request.POST['username']
            password=request.POST['password']

            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.info(request,'Username or Password incorrect!!')
    return render(request,'accounts/login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')
    
@login_required(login_url='login')
def Edit(request,pk):
    # display=Clients.objects.filter(id=pk).values()
    # context={'dis':display}
    client=Clients.objects.get(id=pk)
    form=ClientsForm(instance=client)
    if request.method=='POST':
        form=ClientsForm(request.POST,instance=client)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'accounts/edit.html',{'form':form})

def Create_Client(request):
    # display=Clients.objects.filter(id=pk).values()
    # context={'dis':display}
    form=ClientsForm()
    form.fields['gymUser'].initial=request.user.id
    
    if request.method=='POST':
        form=ClientsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'accounts/edit.html',{'form':form})

def Delete(request,pk):
    client=Clients.objects.get(id=pk)
    if request.method=='POST':
       client.delete()
       return redirect('/')
    return render(request,'accounts/delete.html',{'client':client})

def Bmi(request,pk):
    client=Clients.objects.get(id=pk)
    weight=client.weight
    height=client.height
    height=height/100
    bmi=weight/(height**2)
    bmi=round(bmi,3)
    text=""
    diet=""
    Example=""

    if bmi<16:
        text='Severly underwieght'
        diet="""Starchy vegetables, dense whole grains, proteins low in saturated
fat and low-fat dairy."""
        Example="""Example: carrot, tomato, barley, rice porridge, milk, yogurt,
cheese, bread, wheat flour, noodle, rice flour"""
    elif(bmi >= 16 and bmi < 18.5):
        text='Underweight'
        diet="""Starchy vegetables, dense whole grains, proteins low in saturated
fat and low-fat dairy."""
        Example="""Example: carrot, tomato, barley, rice porridge, milk, yogurt,
cheese, bread, wheat flour, noodle, rice flour"""
    elif(bmi >= 18.5 and bmi < 25):
        text='Healthy'
        diet="""Fruits, vegetables, whole-grains, legumes, nuts and seeds, meat,
poultry and fish."""
        Example="""Example: apple, banana, grapes, bread, soya bean curd, soya bean
milk, dhal, anchovy, fish ball, crab, cuttlefish."""
    elif(bmi >= 25 and bmi < 30):
        text='Overweight'
        diet="""Whole grains, fresh produce, beans and nuts, fish, fruits and
vegetables."""
        Example="""Example: oat, barley, coconut water, peanut, almond, fish ball,
grilled fish, green apple, banana, orange, mango, carrot, papaya."""
    else:
        text='Severly Overweight'
        diet="""Vegetables, high fibre food, whole grains, lean proteins and fruits."""
        Example="""Example: brown rice, whole-wheat pasta, wheat bread, broccoli,
legumes and spinach, tofu, fish, shellfish."""

    recommended={'text':text,'diet':diet,'example':Example}
    context={'bmi':bmi,'client':client,'text':text,'recommended':recommended}
    return render(request,'accounts/bmi.html',context)

def index(request):
    return render(request,'accounts/index.html')
