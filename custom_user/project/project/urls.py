from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from project.views import adminPage, homePage,loginPage,sign_upPage,logoutPage, userPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homePage,name="homePage"),
    path('adminPage',adminPage,name="adminPage"),
    path('userPage',userPage,name="userPage"),
    path('loginPage',loginPage,name="loginPage"),
    path('sign_upPage',sign_upPage,name="sign_upPage"),
    path('logoutPage',logoutPage,name="logoutPage"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
