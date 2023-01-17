from django.contrib.auth import get_user_model
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import IsAdminUser

from .permissions import IsProfileAuthor
from .serializers import ProfileSerializer, ProfileUpdateSerializer, UserSerializer
User = get_user_model()


class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser, ]


class ProfileRetrieveAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsProfileAuthor,)


class ProfileUpdateAPIView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileUpdateSerializer
    permission_classes = (IsProfileAuthor,)