from django.shortcuts import render, redirect
from account.models import User
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login as auth_login

# Create your views here.

def index(request):
    return render(request,'core/index.html')


def login(request):

    if request.method == 'POST':
        email = request.POST.get('email','')
        password = request.POST.get('password','')

        if email and password:
            user = authenticate(email=email, password=password)

            if user is not None:

                auth_login(request, user)

                return redirect("/account/home/")

    return render(request,'core/login.html')

def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        if not password or not first_name or not last_name or not email:
            messages.error(request, "All fields are required")

        else:
            try:
                User.objects.create(first_name=first_name, last_name=last_name, email=email, password=make_password(password))
                messages.success(request, "Registration successful")
                
            except Exception as e:
                messages.error(request, str(e))

    return render(request,'core/register.html')





def dashboard(request):
    return render('core/dashboard.html')