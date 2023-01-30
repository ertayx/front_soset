from rest_framework.permissions import BasePermission, SAFE_METHODS
from django.contrib.auth import get_user_model

User = get_user_model()


class IsProfileAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):

        student_list = User.objects.get(id=request.user.id).student.all()
        
        return (obj.id == request.user.id) or (obj in student_list)


       
