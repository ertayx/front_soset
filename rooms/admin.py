from django.contrib import admin

from .models import Room, Lessons, Tasks, Answers, Essa, CaseWork

admin.site.register(Lessons)
admin.site.register(Tasks)
admin.site.register(Answers)
admin.site.register(CaseWork)

class EssaModelAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        kwargs["queryset"] = request.user.student.all()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class RoomAdmin(admin.ModelAdmin):

    def save_related(self, request, form, formsets, change):
        super(RoomAdmin, self).save_related(request, form, formsets, change)

        lessons_query = Lessons.objects.filter(level=form.instance.level)
        
        count = form.instance.count_lessons
        i = 0
        for lesson in lessons_query:
            if i == count or count < 1:
                i = 0
                break
            form.instance.lessons.add(lesson)
            i+=1
       
admin.site.register(Room, RoomAdmin)
admin.site.register(Essa)
