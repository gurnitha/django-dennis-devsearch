# users/views.py

# Django modules
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm

# Locals
from . models import Profile, Skill 
from projects.models import Tag
from . forms import CustomUserCreationForm

# Create your views here.

# loginUser view
def loginUser(request):

	# Don't show logn page to LOGGED IN user or
	# redirect logged in user to profiles page
	if request.user.is_authenticated:
		return redirect('users:profiles')

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
		#    or the credentials is not correct
		#    show flash message
		except:
			messages.error(request, 'Username does not exitst!')

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
			messages.error(request, 'Username OR password is incorrect. Try it again ...')
			return redirect('users:login')


		''' NOTE:
			If username and password NOT CORRECT it will show messages like this:
			---------
			Username does not exitst!
			Username OR password is incorrect. Try it again ... 
			---------
		'''
	
	return render(request, 'users/login_register.html')
	

# logoutUser view
def logoutUser(request):
	# Kill the session using the logout method
	# and redirect user to login page
	logout(request)
	messages.info(request, 'Your are logged out!')
	return redirect('users:login')


# registerUser view
def registerUser(request):
	page = 'register'
	# form = UserCreationForm
	form = CustomUserCreationForm

	# Logic to register user

	# 1. If the request is POST, then
	#    use UserCreationForm
	if request.method == 'POST':
		# form = UserCreationForm(request.POST)
		form = CustomUserCreationForm(request.POST)

		# 2. Authenticate the form, 
		#    get the user's instance,
		#    create temporary data
		#    and don't save right away,
		#    modify the instances to lowercase
		#    then save the instace.
		if form.is_valid():
			user = form.save(commit=False)
			user.username = user.username.lower()
			user.save()

			# Message
			messages.success(request, 'User account was successfully created!')

			# Automatically Log in user after signing up
			login(request, user)
			return redirect('users:profiles')

		# 3. If register faild
		else:
			messages.success(request, 'An error occurred during registration!')

	context = {
		'page':page,
		'form':form}

	return render(request, 'users/login_register.html', context)


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


# userAccount view
def userAccount(request):
	context = {}
	return render(request, 'users/account.html', context)