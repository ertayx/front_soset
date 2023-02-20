from django.urls import path
from .views import RoomList, RoomDetail

urlpatterns = [
    path('rooms/', RoomList.as_view()),
    path('rooms/<str:name>/', RoomDetail.as_view()),
]