# users/views.py

# Django modules
from django.shortcuts import render

# Locals
from . models import Profile, Skill 
from projects.models import Tag

# Create your views here.

# loginUser view
def loginUser(request):
	# Check if the request is POST
	if request.method == 'POST':
		# Print out the input in the terminal
		print(request.POST)
	
	return render(request, 'users/login_register.html')
	

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

	'''Get skill without description'''
	otherSkills = profile.skill_set.filter(description="")

	tags = Tag.objects.all()

	context = {
		'profile':profile,
		'topSkills':topSkills,
		'otherSkills':otherSkills,
		'tags':tags
	}
	return render(request, 'users/user-profile.html', context)
