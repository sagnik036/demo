from queue import Empty
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import *

def register(request):
    return render (request,'signup.html')


def doctor(request):
    return render (request,'doctor.html')


def signup(request):
    return render (request,'register.html')

def user(request):
    return render (request,'patient.html')

def user_register(request):
    if request.method == 'POST':
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        profile_picture = request.POST["profile_picture"]
        username = request.POST["username"]
        email_id = request.POST["email_id"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        line1 = request.POST["line1"]
        city = request.POST["city"]
        state = request.POST["state"]
        pincode = request.POST["pincode"]

        if password1 == password2:
          user = User_Custom.objects.create(first_name = first_name,last_name=last_name,profile_picture=profile_picture,username=username,
             email_id=email_id,password=password1,line1=line1,city=city,state=state,pincode=pincode
            )
          user.save()
          print("register")
          return redirect('/dashboard')
        else:
            messages.info(request,"password not matching")

    else:
        return redirect('/signup')

    return redirect('/signup')

def dashboard (request):
    return render (request,'dashboard.html')


def login(request):
    if request.method == "POST":
         username = request.POST["username"]
         password = request.POST["password"]

         x=User_Custom.objects.filter(username=username,password=password)
         print(x)

         if x :
            return redirect('/dashboard')
         else:
            messages.info(request,"no user found")

    return render(request,'login.html')