# Generated by Django 5.0.3 on 2024-03-30 00:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_usermodel_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='password',
        ),
    ]
