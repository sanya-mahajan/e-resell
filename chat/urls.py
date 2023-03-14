from django.urls import path

from chat import views

app_name = 'chat'

urlpatterns = [
    path('chat/', views.index, name='index'),
    path('chat/<int:id>/', views.chat_page, name='chat_page'),
]