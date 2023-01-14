from django.shortcuts import redirect
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404, ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser


from .permissions import IsProfileAuthor
from .serializers import RegisterSerializer, ProfileSerializer, ProfileUpdateSerializer, UserSerializer
from rooms.models import Room
User = get_user_model()

class RegisterAPIView(APIView):

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response('Account created', 201)
        

@api_view(["GET"])
def activate(request, activation_code):
    user = get_object_or_404(User, activation_code=activation_code)
    user.is_active = True
    user.activation_code = ''
    user.save()
    return redirect("http://127.0.0.1:3000/")




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