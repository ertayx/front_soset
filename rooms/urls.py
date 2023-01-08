from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import LessonApiView, TasksApiView, AnswersApiView, RoomApiView

router = DefaultRouter()
router.register('lessons', LessonApiView)
router.register('tasks', TasksApiView)
router.register('answers', AnswersApiView)
router.register('rooms', RoomApiView)

urlpatterns = [
    path('', include(router.urls)),
]