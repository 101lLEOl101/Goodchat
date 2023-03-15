from django.db import models
from users.models import User
# Create your models here.


class Post(models.Model):
    """
    Model for user text-posts
    """
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now=True)
    is_edited = models.BooleanField(default=False)


class Comment(models.Model):
    """
    Model for user comments for posts
    """
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now=True)
    is_edited = models.BooleanField(default=False)
