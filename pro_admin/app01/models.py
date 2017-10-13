from django.db import models


# Create your models here.

class UserInfo(models.Model):
    username = models.CharField(max_length=32, verbose_name='用户名')
    email = models.EmailField(max_length=32, verbose_name='邮箱')

    def __str__(self):
        return self.username


class Role(models.Model):
    name = models.CharField(max_length=32, verbose_name='名称')

    def __str__(self):
        return self.name
