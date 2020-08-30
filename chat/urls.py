# chat/urls.py
from django.urls import path

from . import views
from .views import add_message_attachment

urlpatterns = [
    path('', views.index, name='index'),
    path('api/add-message-attachment/', add_message_attachment),
    path('<str:room_name>/<str:user_name>/', views.room, name='room'),
]
