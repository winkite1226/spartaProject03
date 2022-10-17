from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    class Meta:
        db_table = 'user'

    user_name = models.CharField(max_length=30)
    phone = models.IntegerField(default=0)
