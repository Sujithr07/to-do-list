from django.shortcuts import render


def register(request):
    if request.method =='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')

        print(request.POST)


    return render(request,'authentication/register.html')


def login_user(request):
    return render(request,'authentication/login.html')
    
