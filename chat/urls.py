from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import Chat_Room

router = DefaultRouter()
router.register('chat_room', Chat_Room)


urlpatterns = [
    path('', include(router.urls)),
]