from django.contrib.auth import get_user_model
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView


from .permissions import IsProfileAuthor
from .serializers import CustomLoginSerializer, ProfileSerializer, ProfileUpdateSerializer, UserSerializer

User = get_user_model()

class Login(TokenObtainPairView):
    serializer_class = CustomLoginSerializer

class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsProfileAuthor]


    def get_queryset(self):
        student_list = User.objects.get(id=self.request.user.id).student.all()
        return student_list
    

class ProfileRetrieveAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsProfileAuthor,)


class ProfileUpdateAPIView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileUpdateSerializer
    permission_classes = (IsProfileAuthor,)

