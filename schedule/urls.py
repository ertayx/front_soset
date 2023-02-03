from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import TableViewSet

router = DefaultRouter()
router.register('schedule', TableViewSet)

urlpatterns = [
    path('', include(router.urls)),
]