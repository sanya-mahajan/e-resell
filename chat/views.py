from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.http import HttpResponse
from chat.models import Message
from django.contrib.auth.models import User

def index(request):
    user= request.user
    context = {'user': user}
    return render(request, 'chatindex.html', context)


def chat_page(request, id):
    user_object = get_user_model().objects.get(id=id)
    print (user_object)
    users = get_user_model().objects.exclude(id=request.user.id)
    thread_name = (
        f'chat_{request.user.id}_{user_object.id}'
        if int(request.user.id) > int(user_object.id)
        else f'chat_{user_object.id}_{request.user.id}'
    )
    messages = Message.objects.filter(thread_name=thread_name).select_related('sender')
    context = {
        'users': users,
        'user_object': user_object,
        'messages': messages,
        'room_name': id,
    }
    return render(request, 'room.html', context)