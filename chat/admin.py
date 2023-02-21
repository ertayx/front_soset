from django.contrib import admin
from .models import Message, Room, Task_Class_work

# Register your models here.
admin.site.register(Task_Class_work)
admin.site.register(Message)
admin.site.register(Room)