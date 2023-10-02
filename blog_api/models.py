from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title
