# users/views.py

# Django modules
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

# Locals
from . models import Profile, Skill 
from projects.models import Tag

# Create your views here.

# loginUser view
def loginUser(request):
	# 1. If POST request, get the input data
	#    that is the username and password
	if request.method == 'POST':
		# (Optional) Print out the input in the terminal
		# print(request.POST)

		username = request.POST['username']
		password = request.POST['password']

		# 2. Use 'try block' to check if the input data exist 
		# or not in the db, then return user
		try:
			user = User.objects.get(username=username)
		# 3. If user does not exist in db
		# or the credentials is not correct
		except:
			print('Username does not exitst!')

		# 4. If user exists, authenticate it, then return user
		user = authenticate(
			request,
			username=username,
			password=password)

		# 5. If authenticated (user does exist), log the user in
		# and redirect him to any page you want
		if user is not None:
			# This login will create session in the db
			# and the session will use it in the browser
			login(request, user)
			return redirect('users:profiles')

		# 6. If user exist, but its credentials incorrect
		else:
			print('Username OR password is incorrect. Try it again ...')
			return redirect('users:login')
	
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
