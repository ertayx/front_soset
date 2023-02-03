from rest_framework.viewsets import ModelViewSet
from .serializers import TableSerializer
from .models import Table
from rest_framework.permissions import IsAdminUser
from django.shortcuts import get_object_or_404
from rooms.models import Room
from rest_framework.response import Response

class TableViewSet(ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    # permission_classes = [IsAdminUser]


    def create(self, request, *args, **kwargs):
        user = request.user
        # print(user.is_teacher)
        if not user.is_teacher:
            # user = request.user
            weekday = request.data.get('weekday')
            time = request.data.get('time')
            room_id = user.user_room.all()
            for i in room_id:
                if user == i.user:
                    i.id
            room = get_object_or_404(Room, id=i.id)
            qury = Table.objects.create(
                weekday=weekday,
                time = time,
                room=room
            )
            serializer = TableSerializer(qury)
            return Response(serializer.data)
        else:
            weekday = request.data.get('weekday')
            time = request.data.get('time')
            room_id = user.user_room.all()
            for i in room_id:
                if user == i.user:
                    i.id
            room = get_object_or_404(Room, id=i.id)
            qury = Table.objects.create(
                weekday=weekday,
                time=time,
                room=room,
                accepted=True
            )
            serializer = TableSerializer(qury)
            return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        user = request.user
        queryset = self.queryset
        a = []
        if user.is_teacher:
            for i in queryset:
                if i.room.user.studen_users.exists():
                    serializer = TableSerializer(i)
                    a.append(serializer.data)
        
            return Response(a)
        for i in queryset:
            if i.room.user == user:
                serializer = TableSerializer(i)
                a.append(serializer.data)
        return Response(a)