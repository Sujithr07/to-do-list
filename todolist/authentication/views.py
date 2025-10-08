from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def register(request):

    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method =='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')


        user_data_has_error= False

        if User.objects.filter(username=username).exists():
            messages.error(request,'username already exists')
            user_data_has_error= True
            
        if User.objects.filter(email=email).exists():
            messages.error(request,'email already exists')
            user_data_has_error= True

        if password!=confirm_password:
            user_data_has_error= True
            messages.error(request,'password does not match')

        if user_data_has_error:  
            return redirect('register')

        user=User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user.save()
        messages.success(request,"account has been created, log in")
        return redirect('login')

    return render(request,'authentication/register.html')

def login_user(request):

    if request.user.is_authenticated:
        return redirect('home')


    if request.method=='POST':

        username=request.POST.get('username')
        password=request.POST.get('password')

        if not (username and password):
            return redirect('login')

        user=authenticate(request=request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')

        else:
            messages.error(request,'inavlid username or password')
            return redirect('login')

    return render(request,'authentication/login.html')

@login_required  
def home(request):
    return HttpResponse("you r authenticated <br><a href='/logout'>Logout</a>")


def logout_user(request):
    logout(request)
    return redirect('login')