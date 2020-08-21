from django.db import models
from users.models import MyUser

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(MyUser,on_delete = models.CASCADE)
	image = models.ImageField(default = 'default.jpg',upload_to = 'profile_pics')

	def __str__(self):
		return f'{self.user.username} Profile'