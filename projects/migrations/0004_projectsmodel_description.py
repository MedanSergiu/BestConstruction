# Generated by Django 5.0.3 on 2024-03-30 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_rename_projectmodel_projectsmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectsmodel',
            name='description',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
