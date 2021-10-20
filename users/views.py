# users/views.py

# Django modules
from django.shortcuts import render

# Locals
from . models import Profile, Skill 

# Create your views here.

# Profiles view
def profiles(request):
	profiles = Profile.objects.all()
	skills = Skill.objects.all()
	context = {
		'profiles':profiles,
		'skills': skills
	}
	return render(request, 'users/profiles.html', context)


# userProfile view
def userProfile(request, pk):
	profile = Profile.objects.get(id=pk)

	'''Exclude skill that has not description or
	   get skill with descripion'''
	topSkills = profile.skill_set.exclude(description__exact="")

	context = {
		'profile':profile,
		'topSkills':topSkills
	}
	return render(request, 'users/user-profile.html', context)
