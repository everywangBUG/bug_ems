from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    mobile = models.CharField(max_length=15, unique=True, verbose_name='手机号码')
    avatar = models.ImageField(upload_to='avatar', verbose_name='用户头像')

    class Meta:
        db_table = 'user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        
    def __str__(self) -> str:
        return self.mobile