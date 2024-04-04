from django.db import models

# Create your models here.

class ContactModel(models.Model):
    full_name = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=10, null=False)
    email = models.EmailField(null=False, unique=True)
    Text = models.CharField(max_length=1000, null=False)