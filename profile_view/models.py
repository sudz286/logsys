from django.db import models
from users.models import MyUser
from annoying.fields import AutoOneToOneField
from PIL import Image

# Create your models here.
class Profile(models.Model):
	user = AutoOneToOneField(MyUser,on_delete = models.CASCADE,primary_key = True)
	image = models.ImageField(default = 'default.jpg',upload_to = 'profile_pics')

	def __str__(self):
		return f'{self.user.username} Profile'

	def save(self, *args, **kwargs):
		super(Profile, self).save(*args, **kwargs)

		img = Image.open(self.image.path)

		if img.height > 300 or img.width > 250:
			output_size = (300,250)
			img.thumbnail(output_size)
			img.save(self.image.path)
