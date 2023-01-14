from django.db import models

from rooms.models import Room

# Create your models here.

class Table(models.Model):
    room = models.ForeignKey(Room, verbose_name='table', on_delete=models.SET_NULL, null=True)
    time = models.DateTimeField(blank=True, null=True)
    message = models.CharField(blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.room}-->{self.time}'
