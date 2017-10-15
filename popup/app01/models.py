from django.db import models

class UserGroup(models.Model):
    title = models.CharField(max_length=32, verbose_name='用户组')

    def __str__(self):
        return self.title