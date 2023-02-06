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
from rest_framework.pagination import PageNumberPagination
from schedule.serializers import TableSerializer

User = get_user_model()

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 2


class CustomPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 2
    

    def get_paginated_response(self, data):
            return Response({
                'links': {
                    'next': self.get_next_link(),
                    'previous': self.get_previous_link()
                },
                'count': self.page.paginator.count,
                'results': data
            })

class EssaApiView(ModelViewSet):
    queryset = Essa.objects.all()
    serializer_class = EssaSerializer
    permission_classes = [IsEssaAuthor]


    def get_queryset(self):
        if self.request.user.is_teacher:
            essa = Essa.objects.filter(teacher = self.request.user)
        else:
            essa = Essa.objects.filter(student = self.request.user)
        return essa

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)
        

class CaseWorkView(ModelViewSet):
    queryset = CaseWork.objects.all()
    serializer_class = CaseWorkSerializer
    permission_classes = [IsAdminUser]
    pagination_class = CustomPagination

    @action(['GET',], detail=True)
    def get_task(self, requset, pk):
        case = self.get_object()
        for i in case.tasks_case.all():
            print(i.case_work, '!!!!!!!!')
            if i.case_work.exists():
                return Response(f'{i}') 
        return Response(f'{case.tasks_case}')


class RoomApiView(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsRoomOwner, ]

    @action(['PUT','PATCH', 'GET'], detail=True)
    def accept_schedule(self, request, pk):
        room = self.get_object()
        print(room.table_room.all())
        val = []
        for i in room.table_room.all():
            serializer = TableSerializer(i)
            val.append(serializer.data)
        return Response(val)

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
    pagination_class = StandardResultsSetPagination

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


class Task_CaseApiView(ModelViewSet):
    queryset = CaseWork.objects.all()
    serializer_class = CaseWorkSerializer
    
    def retrieve(self, request, *args, **kwargs):
        params = request.GET.get('task')

        if params:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            data = serializer.data
            try:
                res = data['tasks'][int(params)-1]
                return Response(res, 200)
            except:
                return Response('Powel nahui Ertay', 400)
        else:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
        return Response(serializer.data)
