from django.db import models

from rooms.models import Room

# Create your models here.

class Table(models.Model):
    WEEKDAY_CHOICE = (
        ('monday', 'monday'),
        ('tuesday', 'tuesday'),
        ('wednesday','wednesday'),
        ('thursday','thursday'),
        ('friday','friday'),
        ('saturday', 'saturday'),
        ('sunday', 'sunday'),
    )
    time = models.TimeField(blank=True, null=True)
    # message = models.CharField(blank=True, null=True)
    weekday = models.CharField(choices=WEEKDAY_CHOICE, max_length=50)
    accepted = models.BooleanField(default=False)
    room = models.ForeignKey(
        Room, 
        related_name='table_room', 
        on_delete=models.CASCADE)
    


    def __str__(self) -> str:
        return f'{self.room}-->{self.time} --> {self.weekday}'
