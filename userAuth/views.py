
from django.shortcuts import render,HttpResponse,redirect
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from rest_framework import generics, serializers
from django.contrib.auth import authenticate,logout,login #in built user model
from django.contrib.auth.models import User
from .serializers import UserSerializer
from django.contrib.auth.forms import AuthenticationForm

class userslist(generics.ListCreateAPIView):
	queryset=User.objects.all()
	serializer_class=UserSerializer



def loginusr(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("homepage")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})


def logoutusr(request):
    logout(request)
    return render(request,'logout.html')


def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect('homepage')
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})    

