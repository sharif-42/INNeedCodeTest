from django.db import models
from django.contrib.auth.models import User


class UserFileManager(models.Manager):
    def create_user_file(self,user, requested_file):
        return self.create(
            user= user,
            file = requested_file
        )

class UserFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    file = models.ImageField(upload_to='images')
    created_at = models.DateTimeField(auto_now_add=True)
    objects = UserFileManager()

    class Meta:
        verbose_name = 'User File'
        verbose_name_plural = 'User Files'

    def __str__(self):
        return str(self.user)
