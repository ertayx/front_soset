from rest_framework.permissions import BasePermission, SAFE_METHODS
from django.contrib.auth import get_user_model

User = get_user_model()

class IsRoomOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.user


class IsEssaAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['PATCH', 'PUT'] and not request.user.is_teacher:
            print(111)
            return obj.students.filter(id=request.user.id).exists()
        if not request.user.is_authenticated:
            print(222)
            return False
        if request.method in SAFE_METHODS:
            print(333)
            return obj.students.filter(id=request.user.id).exists()
        print(444)
        return request.user.is_teacher