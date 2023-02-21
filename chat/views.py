from asgiref.sync import sync_to_async
from django.shortcuts import render, reverse, get_object_or_404
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet

from .models import Room, Message
from .serializers import RoomSerializer

User = get_user_model()

class Chat_Room(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
