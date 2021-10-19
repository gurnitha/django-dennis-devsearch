# users/views.py

# Django modules
from django.shortcuts import render

# Locals
from . models import Profile, Skill 

# Create your views here.

# Profile view
def profiles(request):
	profiles = Profile.objects.all()
	skills = Skill.objects.all()
	context = {
		'profiles':profiles,
		'skills': skills
	}
	return render(request, 'users/profiles.html', context)