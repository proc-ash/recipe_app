from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import *
# Create your views here.

def home(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        user_password = request.POST['user_password']
        confirm_password = request.POST['confirm_password']

        #check if user already exist or not
        user = User.objects.filter(username = username )
        if user.exists():
            messages.info(request, 'Username already exist')
            return redirect('signup')

        #if user password and confirm password are same then create the user
        if user_password == confirm_password:
            user = User.objects.create( 
                first_name = fname,
                last_name = lname,
                username = username,
                email = email
            )
            user.set_password(user_password)
            user.save()
            messages.success(request, 'your account has been successfully created')

            return redirect('signin')
        else:
            messages.error(request, 'password and confirm password didn\'t match') 
            return redirect('signup')
    return render(request, 'signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        user_password = request.POST['password']

        #check if password is correct or not
        if not User.objects.filter(username = username).exists():
            messages.error(request,'Username doesn\'t exist')
            return redirect('login')

        user = authenticate(username = username, password = user_password)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return redirect('dishes/')
        else:
            messages.error(request,'Bad credentials')
            return redirect('login')
    return render(request, 'signin.html')

def signout(request):
    logout(request)
    return render(request, 'index.html')
