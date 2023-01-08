from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from account.models import User
from .models import Lessons, Tasks, Answers, Room
from .serializers import LessonSerializer, TasksSerializer, AnswersSerializer, RoomSerializer
from .permissions import IsRoomOwner


class RoomApiView(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsRoomOwner, ]

    def get_queryset(self):
        return Room.objects.filter(user = self.request.user)
    

class LessonApiView(ModelViewSet):
    queryset = Lessons.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAdminUser, ]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context

    
class TasksApiView(ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer
    permission_classes = [IsAdminUser, ]

    
class AnswersApiView(ModelViewSet):
    queryset = Answers.objects.all()
    serializer_class = AnswersSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Answers.objects.filter(user = self.request.user)
    
    def perform_create(self, serializer):
        task = self.request.data.get('tasks')
        answer = self.request.data.get('answer')
        user = self.request.user

        task = get_object_or_404(Tasks, id=task)
        
        if task.right_answer == answer:
            accepted_bool = True
        else:
            accepted_bool = False
        
        instance = Answers.objects.create(
            answer = answer,
            user = user,
            accepted = accepted_bool
            )
        instance.tasks.add(task) 

        return Response('ok')
        
        