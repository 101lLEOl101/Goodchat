from django.db import models
from users import User

# Create your models here.
class Chat(models.Model):
    pass


class MultyChat(Chat):
    name = models.CharField(verbose_name='chat name', max_length=50)


class DuoChat(Chat):
    member1 = models.ForeignKey(to=User, verbose_name='first member')
    member2 = models.ForeignKey(to=User, verbose_name='second member')
    