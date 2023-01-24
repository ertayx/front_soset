from django.db import models
from account.models import User, Student

class Essa(models.Model):
    teacher = models.ForeignKey(User, related_name='essays', on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=1000)
    text = models.TextField(max_length=3000, blank=True)
    students = models.ManyToManyField(Student, related_name='essays')

class Room(models.Model):
    LEVEL_CH = (
        ('elem', 'elementary'),
        ('pre', 'pre-intermediate'),
        ('inter', 'intermediate'),
        ('upper', 'upper-intermediate'),
        ('adv', 'advanced')
    )

    level = models.CharField(choices=LEVEL_CH, default='elem', max_length=50)
    user = models.ForeignKey(User, related_name='user_room', on_delete=models.DO_NOTHING)
    lessons = models.ManyToManyField('Lessons', related_name='room_lesson', blank=True)
    progress = models.IntegerField(default=0)
    payment = models.IntegerField(default=0)
    count_lessons = models.IntegerField(default=0)
    

    def __str__(self) -> str:
        return f'{self.user} --> {self.level}'



class Lessons(models.Model):
    SECTION = (
        ('HW', 'homework'),
        ('CW', 'classwork')
    )

    LEVEL_CH = (
        ('elem', 'elementary'),
        ('pre', 'pre-intermediate'),
        ('inter', 'intermediate'),
        ('upper', 'upper-intermediate'),
        ('adv', 'advanced')
    )

    case_work = models.CharField(choices=SECTION, max_length=30)
    title = models.CharField(max_length=50)
    level = models.CharField(choices=LEVEL_CH, default='elem', max_length=50)

    def __str__(self) -> str:
        return f'{self.title}-->{self.case_work} --> {self.level}'

class CaseWork(models.Model):
    CASECHOISE = (
        ('first', 'first'),
        ('second', 'second'),
        ('third', 'third'),
        ('fourth','fourth')
    )

    title = models.CharField(choices=CASECHOISE, max_length=30)

    def __str__(self) -> str:
        return f'{self.title}'

class Tasks(models.Model):
    lessons = models.ForeignKey(Lessons, related_name='task_lesson', on_delete=models.RESTRICT)
    right_answer = models.CharField(max_length=150)
    flag = models.IntegerField(default=0)
    description = models.TextField()
    case_work = models.ForeignKey(CaseWork, related_name='tasks_case', on_delete=models.DO_NOTHING)
    def __str__(self) -> str:
        return f'{self.right_answer} -->{self.lessons}'


class Answers(models.Model):
    answer = models.TextField()
    user = models.ForeignKey(User, related_name='answer_user',on_delete=models.DO_NOTHING,blank=True)
    tasks = models.ManyToManyField(Tasks, related_name='task_answer')
    accepted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.tasks}-->{self.user}'

