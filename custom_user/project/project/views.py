
from django.contrib import messages #for massages pass
from django.http import HttpResponse
from django.shortcuts import redirect,render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from app.models import *


def homePage(req):
    return render(req,"index.html")

@login_required
def adminPage(req):
    Cuser = req.user
    if Cuser.user_type == "admin":
        return render(req,"adminPage.html")
    else:
        messages.warning(req,'Your user type is not bloger..')
        return redirect("homePage")

@login_required
def userPage(req):
    Cuser = req.user
    if Cuser.user_type == "user":
        return render(req,"userPage.html")
    else:
        messages.warning(req,'Your user type is not viewer..')
        return redirect("homePage")

def loginPage(req):
    if req.method == "POST":
        Username=req.POST.get("username")
        pas=req.POST.get("password")

        user=authenticate(username=Username,password=pas)

        if user:
            login(req, user)
            messages.success(req,'Login Successful!')
            return redirect('homePage')
        else:
            messages.warning(req,"your username and password is roong")
            return render(req,"loginPage.html")
    return render(req,"loginPage.html")

def sign_upPage(req):
    if req.method == "POST":
        user_type=req.POST.get("user_type")
        First_name=req.POST.get("first_name")
        Last_name=req.POST.get("last_name")
        username=req.POST.get("username")
        email=req.POST.get("email")
        password=req.POST.get("password")
        confirm_password=req.POST.get("confirm_password")

        if all([user_type, First_name, Last_name, username, email, password, confirm_password]):
            if password == confirm_password:
                user=User_Model.objects.create_user(
                    user_type = user_type,
                    first_name = First_name,
                    last_name = Last_name,
                    username = username,
                    password = confirm_password
                )
                messages.success(req, 'Registration Successful!')
                return render(req,'loginPage.html')
            else:
                messages.warning(req, 'Password not matched!')
                return render(req,'sign_upPage.html')
        else:
            messages.warning(req, 'All fields are required!')
            return render(req,'sign_upPage.html')
    return render(req,"sign_upPage.html")

def logoutPage(req):
    logout(req)
    messages.success(req,'Logout Successful!')
    return render(req,"loginPage.html")
