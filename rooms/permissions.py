from rest_framework.permissions import BasePermission
from django.contrib.auth import get_user_model

User = get_user_model()

class IsRoomOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.user


class IsEssaAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        student_list = User.objects.get(id=request.user.id).student.all()
        return (obj.student == request.user) or (obj.student in student_list)