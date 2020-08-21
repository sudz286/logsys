from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm
from django.contrib import messages

# Create your views here.
@login_required
def home(request):
	if request.method == 'POST':
		profile_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)
		if profile_form.is_valid():
			profile_form.save()
			messages.success(request,f'Account has been updated')
			return redirect('home')

	else:
		profile_form = ProfileUpdateForm(instance = request.user.profile)

	context = {'profile_form':profile_form}
	return render(request,'profile_view/home.html', context)