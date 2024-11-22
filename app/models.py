from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    title = models.CharField(max_length=1000)
    author = models.CharField(max_length=1000)
    description = models.TextField()

    def __str__(self):
        return f"{self.title}"
