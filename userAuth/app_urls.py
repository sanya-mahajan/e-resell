from django.contrib import admin
from django.urls import path
from userAuth import views

urlpatterns = [
    path('users',views.userslist.as_view()),
    path('login',views.loginusr,name="loginpage"),
    path('logout',views.logoutusr,name="logoutpage"),
    path('register',views.register,name="registerpage"),
    

]
