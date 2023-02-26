from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to="images/profile/")
    about = models.CharField(max_length = 500)
    country = models.TextField()
    city = models.TextField()
    education = models.TextField()
    company = models.TextField()
    hobby = models.TextField()