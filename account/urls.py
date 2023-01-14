from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterAPIView, activate, ProfileRetrieveAPIView, ProfileUpdateAPIView, UserListAPIView


urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('activate/<str:activation_code>/', activate),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('users/', UserListAPIView.as_view()),
    path('profile/<int:pk>/', ProfileRetrieveAPIView.as_view()),
    path('profile/update/<int:pk>/', ProfileUpdateAPIView.as_view()),
]