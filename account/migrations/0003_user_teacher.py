# Generated by Django 4.1.5 on 2023-01-11 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_user_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='teacher',
            field=models.BooleanField(default=False),
        ),
    ]