from django.contrib import admin
from django.urls import path

from project.views import homePage, loginPage, logoutPage, sign_upPage


urlpatterns = [
    path('admin', admin.site.urls),
    path('',homePage,name="homePage"),
    path('loginPage',loginPage,name="loginPage"),
    path('sign_upPage',sign_upPage,name="sign_upPage"),
    path('logoutPage',logoutPage,name="logoutPage"),

]
