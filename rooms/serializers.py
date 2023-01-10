from rest_framework import serializers
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from .models import Room, Lessons, Tasks, Answers

User = get_user_model()


class RoomSerializer(serializers.ModelSerializer):
    lessons = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='lessons-detail'
    )

    class Meta:
        model = Room
        fields = '__all__'
         
    def to_representation(self, instance):
        rep =  super().to_representation(instance)
        filt = Answers.objects.filter(user=instance.user)
        rep['progress'] = filt.filter(accepted=True).count()
        

        return rep


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lessons
        fields = '__all__'

    def to_representation(self, instance):
 
        rep = super().to_representation(instance)
        rep['tasks'] = TasksSerializer(instance.task_lesson, many=True).data
        
        return rep


class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'

    def to_representation(self, instance):

        rep = super().to_representation(instance)
        rep['title'] = f'{instance.lessons.title} {instance.id}'
        rep['answers'] = AnswersSerializer(instance.task_answer, many=True).data

        return rep


class AnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = '__all__'
