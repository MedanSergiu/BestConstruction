# Generated by Django 5.0.2 on 2024-03-13 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsLetterModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('date_period', models.CharField(max_length=10)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='media/')),
            ],
        ),
    ]
