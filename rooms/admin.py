from django.contrib import admin

from .models import Room, Lessons, Tasks, Answers, Essa

admin.site.register(Lessons)
admin.site.register(Tasks)
admin.site.register(Answers)

class RoomAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        
        count = form.instance.payment / 900
        form.instance.count_lessons = count

        super(RoomAdmin, self).save_model(request, obj, form, change)

    def save_related(self, request, form, formsets, change):
        super(RoomAdmin, self).save_related(request, form, formsets, change)

        lessons_query = Lessons.objects.filter(level=form.instance.level)
        
        count = form.instance.payment / 900
        i = 0
        for lesson in lessons_query:
            if i == count or count < 1:
                i = 0
                break
            form.instance.lessons.add(lesson)
            i+=1
       
admin.site.register(Room, RoomAdmin)
admin.site.register(Essa)
