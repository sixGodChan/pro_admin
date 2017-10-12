from django.db import models


# Create your models here.

class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    email = models.EmailField(max_length=32)

    def __str__(self):
        return self.username


class Role(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name
