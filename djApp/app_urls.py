

from django.urls import path
from djApp import views #app view 


urlpatterns = [
    
    path('',views.index,name='homepage'),
]
