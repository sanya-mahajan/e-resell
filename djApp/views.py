
from django.urls import reverse
from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
#rendering for response as templates
from datetime import datetime
from django.contrib.auth.models import User
from userAuth import views #for using the login view
from django import forms
from django.contrib.auth.decorators import login_required
#attributs views.attribute




from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def index(request):
    username = ''
    if request.user.is_authenticated:
        username = request.user.username
    context={'uname':username}
    return render(request,'index.html',context)
 

