# Generated by Django 4.1.5 on 2023-01-23 09:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CaseWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('first', 'first'), ('second', 'second'), ('third', 'third'), ('fourth', 'fourth')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Lessons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_work', models.CharField(choices=[('HW', 'homework'), ('CW', 'classwork')], max_length=30)),
                ('title', models.CharField(max_length=50)),
                ('level', models.CharField(choices=[('elem', 'elementary'), ('pre', 'pre-intermediate'), ('inter', 'intermediate'), ('upper', 'upper-intermediate'), ('adv', 'advanced')], default='elem', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('right_answer', models.CharField(max_length=150)),
                ('flag', models.IntegerField(default=0)),
                ('description', models.TextField()),
                ('case_work', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='tasks_case', to='rooms.casework')),
                ('lessons', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='task_lesson', to='rooms.lessons')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(choices=[('elem', 'elementary'), ('pre', 'pre-intermediate'), ('inter', 'intermediate'), ('upper', 'upper-intermediate'), ('adv', 'advanced')], default='elem', max_length=50)),
                ('progress', models.IntegerField(default=0)),
                ('payment', models.IntegerField(default=0)),
                ('count_lessons', models.IntegerField(default=0)),
                ('lessons', models.ManyToManyField(blank=True, related_name='room_lesson', to='rooms.lessons')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_room', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Essa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField(max_length=1000)),
                ('text', models.TextField(blank=True, max_length=3000)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='essa')),
            ],
        ),
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField()),
                ('accepted', models.BooleanField(default=False)),
                ('tasks', models.ManyToManyField(related_name='task_answer', to='rooms.tasks')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='answer_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
