from django.db import models

# Create your models here.

class UserModel(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    second_name = models.CharField(max_length=50, null=False)
    phone = models.CharField(max_length=10, null=True)
    email = models.EmailField(null=False, unique=True)
    description = models.CharField(max_length=1000, null=True)

