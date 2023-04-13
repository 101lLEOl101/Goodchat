from django.db import models
from django.utils.translation import gettext_lazy as _
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
    
    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')


class Comment(models.Model):
    """
    Model for user comments for posts
    """
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now=True)
    is_edited = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')


class Bookmark(models.Model):
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
