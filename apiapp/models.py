from django.db import models

# Create your models here.

class todo_data(models.Model):
    title = models.CharField(max_length= 100)
    description = models.TextField()
    status = models.CharField(max_length=12)

class user_cred(models.Model):
    username = models.CharField(max_length=30, blank=False, unique=True)
    password = models.CharField(max_length=100, blank=False)
