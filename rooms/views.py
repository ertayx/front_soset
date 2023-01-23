from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
# from account.models import User
from .models import Lessons, Tasks, Answers, Room, Essa, CaseWork
from .serializers import LessonSerializer, TasksSerializer, AnswersSerializer, RoomSerializer, EssaSerializer, CaseWorkSerializer
from .permissions import IsRoomOwner, IsEssaAuthor
from django.contrib.auth import get_user_model

User = get_user_model()

class EssaApiView(ModelViewSet):
    queryset = Essa.objects.all()
    serializer_class = EssaSerializer
    permission_classes = [IsEssaAuthor]

    def get_queryset(self):
        rooms = Essa.objects.filter(user = self.request.user)
        return rooms

class CaseWorkView(ModelViewSet):
    queryset = CaseWork.objects.all()
    serializer_class = CaseWorkSerializer
    permission_classes = [IsAdminUser]

class RoomApiView(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsRoomOwner, ]

    def get_queryset(self):
        rooms = Room.objects.filter(user = self.request.user)
        return rooms
    

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

    @action(['POST', 'DELETE'], detail=True)
    def answer(self, request, pk):
        task = self.get_object()
        user = request.user
        answer = request.data
        qury = task.lessons.room_lesson.all()
        net = []
        if request.method == 'POST':
            for i in qury:
                if user == i.user:
                    if task.right_answer == answer.get('answers'):
                        accepted_bool = True
                    else:
                        accepted_bool = False
                    
                    instance = Answers.objects.create(
                        answer = answer.get('answers'),
                        user = user,
                        accepted = accepted_bool,
                        )
                    instance.tasks.add(task)
                    return Response('твой ответ расчитан')
                elif user != i.user:
                    net.append('net')
            if len(net) == len(qury):
                raise Exception('permission denied')
            return Response('ok')
           


class AnswersApiView(ModelViewSet):
    queryset = Answers.objects.all()
    serializer_class = AnswersSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Answers.objects.filter(user = self.request.user)
<<<<<<< HEAD

=======
    
    def perform_create(self, serializer):
        task = self.request.data.get('tasks')
        answer = self.request.data.get('answer')
        user = self.request.user
        print(self.request.data,'!!!')
        task = get_object_or_404(Tasks, id=task)
        qury = task.lessons.room_lesson.all()
        net = []
        for i in qury:
            if user == i.user:
                print(i.user)
                if tasks.right_answer == answer:
                    accepted_bool = True
                else:
                    accepted_bool = False
                
                instance = Answers.objects.create(
                    answer = answer,
                    user = user,
                    accepted = accepted_bool,
                    )      
                instance.tasks.add(t_i) 
                break
            elif user != i.user:
                net.append('net')
        if len(net) == len(qury):
            raise Exception('permission denied')
        return Response('ok')
        
        
>>>>>>> 09eba5d7814687b23c8784455a89868f7849714e
