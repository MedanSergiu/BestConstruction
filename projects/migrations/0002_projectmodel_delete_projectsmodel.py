# Generated by Django 5.0.3 on 2024-03-15 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='media/')),
            ],
        ),
        migrations.DeleteModel(
            name='ProjectsModel',
        ),
    ]
