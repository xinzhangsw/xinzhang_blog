from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)


class Tag(models.Model):
    name = models.CharField(max_length=100)


class Post(models.Model):
    title = models.CharField(max_length=70)
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length=200, blank=True)


category = models.ForeignKey(Category, on_delete=models.CASCADE)
tag = models.ManyToManyField(Tag, blank=True)
author = models.ForeignKey(User, on_delete=models.CASCADE)
