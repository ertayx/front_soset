from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Task_Class_work(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(blank=True)

    def __str__(self) -> str:
        return f'{self.title}'


class Room(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, unique=True)
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name="rooms")
    current_users = models.ManyToManyField(User, related_name="current_rooms", blank=True)
    class_work = models.ForeignKey("Task_Class_work", related_name="classwork_rooms", blank=True,)

    def __str__(self):
        return f"Room({self.name} {self.host})"


class Message(models.Model):
    room = models.ForeignKey("chat.Room", on_delete=models.CASCADE, related_name="messages")
    text = models.TextField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messages")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message({self.user} {self.room})"
