from django.db import models
from django.contrib.auth.models import User
from datetime import date
# Create your models here.

class ArticleRecord(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    heading = models.CharField(max_length=50)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.heading)

class VisitorRecord(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()
    branch = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)
