from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# User model to be used for authentication
class MyUser(AbstractUser):
    pass