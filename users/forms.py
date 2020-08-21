from django import forms
from .models import MyUser
from django.contrib.auth.forms import UserCreationForm
# from phonenumber_field.formfields import PhoneNumberField

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	address = forms.CharField(max_length=300)
	first_name = forms.CharField(max_length=100)
	last_name = forms.CharField(max_length=100)
	phone_no = forms.CharField(max_length=12)

	class Meta:
		model = MyUser
		fields = ['username','email','first_name','last_name','address','phone_no']