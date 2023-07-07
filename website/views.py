from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


# Create your views here.

def home(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        print(f"user is {user}")

        if user is not None:
            login(request, user)
            messages.success(request, "your successfully loged in!!!")
            return redirect("home")
        else:
            messages.success(request, "something error!!..please try again..")
            return redirect("home")
    else:
        return render(request, 'home.html', {})


def login_user(request):
    pass


def logout_user(request):
    logout(request)
    messages.success(request, "ur successfully logged out..")
    return redirect('home')


def register_user(request):
    print('inside register funcc')
    return render(request, 'register.html', {})
