from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class MyUser(AbstractUser):
	address = models.CharField(max_length=300)
	phone_no = models.CharField(max_length=12)