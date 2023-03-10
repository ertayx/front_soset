# Generated by Django 4.1.5 on 2023-02-21 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_alter_message_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task_Class_work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='room',
            name='class_work',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='classwork_rooms', to='chat.task_class_work'),
        ),
    ]
