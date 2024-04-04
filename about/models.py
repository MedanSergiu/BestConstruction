from django.db import models

# Create your models here.


class NewsLetterModel(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    date_period=models.CharField(max_length=10, null=False)
    description = models.TextField(null=False, blank=False)
    image = models.ImageField(upload_to='media/', null=False, blank=False)