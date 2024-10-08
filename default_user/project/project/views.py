from django.shortcuts import render,redirect,HttpResponse
# import for authentication
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required #we need to add LOGIN_URL to sattings.py
# import for create normal user
from django.contrib.auth.models import User 

@login_required
def homePage(req):
    return render(req,"index.html")

def loginPage(req):
    if req.method=="POST":
        user_name=req.POST.get('username')
        pass_word=req.POST.get('password')

        user=authenticate(username=user_name,password=pass_word)

        if user:
            login(req,user)
            return redirect("homePage")
        else:
            return redirect(HttpResponse,"your username and password is rong")
    return render(req,"loginPage.html")

def sign_upPage(req):
    if req.method=="POST":
        user_name=req.POST.get("user_name")
        email=req.POST.get("email")
        password=req.POST.get("password")
        confirm_password=req.POST.get("confirm_password")
        if password==confirm_password:
            user=User.objects.create_user(
                username=user_name,
                email=email,
                password=confirm_password
            )
            return redirect("loginPage")
        else:
            return redirect("homePage")
    return render(req,"sign_upPage.html")

def logoutPage(req):
    logout(req)
    return redirect("loginPage")