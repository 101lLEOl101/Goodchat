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