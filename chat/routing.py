from django.urls import path,re_path
from chat import consumers
websocket_urlpatterns = [
     re_path(r"ws/chat/(?P<room_name>\w+)/$", consumers.chatconsumer.as_asgi()),
]

