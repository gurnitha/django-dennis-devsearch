# users/views.py

# Django modules
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from django.db.models import Q  

# from django.contrib.auth.forms import UserCreationForm

# Locals
from . models import Profile, Message
from projects.models import Tag
from . forms import CustomUserCreationForm, ProfileForm, SkillForm
from .utils import searchProfiles, paginateProfiles

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

		username = request.POST['username'].lower()
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
			# return redirect('users:profiles')
			return redirect(request.GET['next'] if 'next' in request.GET else 'users:account')

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
			return redirect('users:edit-account')

		# 3. If register faild
		else:
			messages.success(request, 'An error occurred during registration!')

	context = {
		'page':page,
		'form':form}

	return render(request, 'users/login_register.html', context)


# Profiles view
def profiles(request):

	# Step 5 Search: use the searchProfiles method
	profiles, search_query = searchProfiles(request)

	# Use the paginateProjects and set the N results (N=2) 
	custom_range, profiles = paginateProfiles(request, profiles, 3)

	# skills = Skill.objects.all()
	context = {
		'profiles':profiles,
		# 'skills': skills,
		'search_query':search_query,
		'custom_range':custom_range
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
@login_required(login_url='login')
def userAccount(request):
	profile = request.user.profile
	skills = profile.skill_set.all()
	# projects = profile.project_set.all()
	projects = profile.project_set.all()
	print(projects)
	context = {
		'profile':profile,
		'skills':skills,
		'projects':projects
	}
	return render(request, 'users/account.html', context)


# editAccount view
@login_required(login_url='login')
def editAccount(request):

	# Get the profile from user
	profile = request.user.profile	

	# Get the attributes from the Profile model
	form = ProfileForm(instance=profile)	

	# If request mothod is POST, process the form
	if request.method == 'POST':
		form = ProfileForm(
					request.POST,
					request.FILES,
					instance=profile)

		# Use is_valid method to check if the form is valid,
		# if the form valid, then save it
		if form.is_valid():
			form.save()

		# Redirect to its account after saving
		return redirect('users:account')

	context = {'form':form}
	return render(request, 'users/profile_form.html', context)


# ---------------------------CRUD SKILL-----------------------

# createSkill view
@login_required(login_url='users:login')
def createSkill(request):

	profile = request.user.profile
	form = SkillForm()
	
	if request.method == 'POST':
		form = SkillForm(request.POST)
		if form.is_valid():
			skill = form.save(commit=False)
			skill.owner = profile
			skill.save()
			messages.success(request, 'Skill was added successfully.')
			return redirect('users:account')

	context = {
		'form':form
	}
	
	return render(request, 'users/skill_form.html', context)



# updateSkill view
@login_required(login_url='users:login')
def updateSkill(request, pk):

	page = 'update'

	profile = request.user.profile
	skill = profile.skill_set.get(id=pk)
	form = SkillForm(instance=skill)
	
	if request.method == 'POST':
		form = SkillForm(request.POST, instance=skill)
		if form.is_valid():
			skill.save()
			messages.success(request, 'Skill was updated successfully.')
			return redirect('users:account')

	context = {
		'form':form,
		'page':page,
	}
	
	return render(request, 'users/skill_form.html', context)



# deleteSkill view
@login_required(login_url='users:login')
def deleteSkill(request, pk):

	profile = request.user.profile
	skill = profile.skill_set.get(id=pk)

	if request.method == 'POST':
		skill.delete()
		messages.success(request, 'Skill was deleted successfully.')
		return redirect('users:account')

	context = {'object':skill}

	return render(request, 'delete_template.html', context)


# ------------------------END CRUD SKILL----------------------


# ------------------------MESSAGES----------------------------

@login_required(login_url='users:login')
def inbox(request):

	# Step 1: Get the logged in user
    profile = request.user.profile
    # Step 2: Get all messages for the receiver
    # NOTE: Do NOT named the var 'messages'. It uses by django
    #       messages is referring to related name in model
    messageRequests = profile.messages.all()
    # Step 3: Check the un-read messages
    unreadCount = messageRequests.filter(is_read=False).count()

    context = {
    	'messageRequests': messageRequests, 
    	'unreadCount': unreadCount
    }
    
    return render(request, 'users/message_inbox.html', context)


@login_required(login_url='login')
def viewMessage(request, pk):

    context = {}

    return render(request, 'users/message.html', context)

# ------------------------END MESSAGES------------------------
