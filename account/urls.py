from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import ProfileRetrieveAPIView, ProfileUpdateAPIView, UserListAPIView, Login


urlpatterns = [
    path('api/token/', Login.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('users/', UserListAPIView.as_view()),
    path('profile/<int:pk>/', ProfileRetrieveAPIView.as_view()),
    path('profile/update/<int:pk>/', ProfileUpdateAPIView.as_view()),
]