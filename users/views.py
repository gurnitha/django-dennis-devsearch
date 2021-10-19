# users/views.py

# Django modules
from django.shortcuts import render

# Locals
from . models import Profile 

# Create your views here.

# Profile view
def profiles(request):
	profiles = Profile.objects.all()
	context = {
		'profiles':profiles
	}
	return render(request, 'users/profiles.html', context)