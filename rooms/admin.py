from django.contrib import admin

from .models import Room, Lessons, Tasks, Answers

admin.site.register(Lessons)
admin.site.register(Tasks)
admin.site.register(Answers)

class RoomAdmin(admin.ModelAdmin):
    def save_related(self, request, form, formsets, change):
        super(RoomAdmin, self).save_related(request, form, formsets, change)
       
        lessons_query = Lessons.objects.filter(level=form.instance.level)
        
     
        for lesson in lessons_query:
            
            if lesson.level == form.instance.level:
                form.instance.lessons.add(lesson)
        
admin.site.register(Room, RoomAdmin)
        