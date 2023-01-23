from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import LessonApiView, TasksApiView, AnswersApiView, RoomApiView, EssaApiView, CaseWorkView

router = DefaultRouter()
router.register('lessons', LessonApiView)
router.register('tasks', TasksApiView)
router.register('answers', AnswersApiView)
router.register('rooms', RoomApiView)
router.register('essa', EssaApiView)
router.register('case', CaseWorkView)


urlpatterns = [
    path('', include(router.urls)),
]