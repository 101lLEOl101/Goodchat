from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from .managers import UserManager
from django.utils.translation import gettext_lazy as _

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_("username"), max_length=50, unique=True)
    email = models.EmailField(_("email"), null=True, blank=True)
    phone = models.CharField(_("phone number"), max_length=25, null = True, blank=True)
    date_joined = models.DateTimeField(_("date joined"), auto_now_add=True)
    is_active = models.BooleanField(_("active"), default=False)
    is_staff= models.BooleanField(_("staff"), default=False)
    
    is_verified = models.BooleanField(_("verifiend"), default=False)
    
    objects = UserManager()
    
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []
    
    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        unique_together = ('username', 'email', 'phone')
    

class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to="images/profile/", default=None)
    about = models.CharField(max_length = 500)
    country = models.TextField(default=None)
    city = models.TextField(default=None)
    education = models.TextField(default=None)
    company = models.TextField(default=None)
    hobby = models.TextField(default=None)
    
