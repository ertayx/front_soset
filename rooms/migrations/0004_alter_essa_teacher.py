# Generated by Django 4.1.5 on 2023-01-28 20:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rooms', '0003_alter_essa_student_alter_essa_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='essa',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teacher_users', to=settings.AUTH_USER_MODEL),
        ),
    ]