# projects/views.py

# Django modules
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# locals
from .models import Project
from .forms import ProjectForm
from .utils import searchProjects

# Create your views here.

def projects(request):

	# Step 5 Search: use the searchProfiles method
	projects, search_query = searchProjects(request)

	# projects = Project.objects.all()
	page_title = 'Projects'
	context = {
		'title':page_title,
		'projects':projects,
		# 'tags':tags,
		'search_query':search_query,
	}
	return render(request, 'projects/projects.html', context)


def project(request, pk):
	projectObj = Project.objects.get(id=pk)
	tags = projectObj.tags.all()
	context = {
		'project':projectObj,
		'tags':tags,
	} 

	return render(request, 'projects/single-project.html', context)



@login_required(login_url="users:login")
def createProject(request):

	# 1. To create project, user MUST logged in first.
	#    Then get profile of the logged in user
	profile = request.user.profile

	# 2. Bring in the ProjectForm class
	form = ProjectForm()

	# 3. If there is POST request, process the form
	if request.method == "POST":

		# Tesing the form: fillin the form and submit it
		# print(request.POST) # tested :)

		# 4. Instantiate the ProjectForm class
		form = ProjectForm(request.POST, request.FILES)
		# 5. Check if form input is valid,
		if form.is_valid():
			# 6. Get instance of the project
			#    and do not save it for now
			project = form.save(commit=False)
			# 7. Update the owner attributes 
			#    of the current project which
			#    has OneToMany rel with profile
			project.owner = profile
			# Save the project
			project.save()
			
			return redirect('projects:projects')



	# # Bring in the ProjectForm class
	# form = ProjectForm()

	# # If there is POST request, process the form
	# if request.method == "POST":

	# 	# Tesing the form: fillin the form and submit it
	# 	# print(request.POST) # tested :)

	# 	# Instantiate the ProjectForm class
	# 	form = ProjectForm(request.POST)
	# 	# Check if form input is valid
	# 	if form.is_valid():
	# 		# Save the input
	# 		form.save()
	# 		return redirect('projects:projects')

	# Context dictionary
	context = {
		'form':form,
	} 

	# Template
	return render(request, 'projects/project_form.html', context)


@login_required(login_url="users:login")
def updateProject(request, pk):

	# 1. To create project, user MUST logged in first.
	#    Then get profile of the logged in user
	#    it represents OneToOne relstionship
	profile = request.user.profile

	# 2. Get the project's instance by its id
	#    that belongs to the logged in user
	#    or get all the projects of that user
	project = profile.project_set.get(id=pk)

	# 3. Instantiate the ProjectForm class
	#    with parameter the instance of the project
	form = ProjectForm(instance=project)

	# 4. If there is POST request, process the form
	if request.method == "POST":

		# Tesing the form: fillin the form and submit it
		# print(request.POST) # tested :)

		# 5. Instantiate the ProjectForm class
		form = ProjectForm(request.POST, request.FILES, instance=project)
		
		# 6. Check if form input is valid
		if form.is_valid():
			# 7. Save the input
			form.save()
			# 8. Redirect the user to projects
			return redirect('projects:projects')

	# # Get the project instance by its id
	# project = Project.objects.get(id=pk)

	# # Instantiate the ProjectForm class
	# # with parameter the instance of the project
	# form = ProjectForm(instance=project)

	# # If there is POST request, process the form
	# if request.method == "POST":

	# 	# Tesing the form: fillin the form and submit it
	# 	# print(request.POST) # tested :)

	# 	# Instantiate the ProjectForm class
	# 	form = ProjectForm(request.POST, instance=project)
	# 	# Check if form input is valid
	# 	if form.is_valid():
	# 		# Save the input
	# 		form.save()
	# 		return redirect('projects:projects')

	# Context dictionary
	context = {
		'form':form,
	} 

	# Template
	return render(request, 'projects/project_form.html', context)


@login_required(login_url="users:login")
def deleteProject(request, pk):

	# 1. To create project, user MUST logged in first.
	#    Then get profile of the logged in user
	#    it represents OneToOne relstionship
	profile = request.user.profile

	# 2. Get the project's instance by its id
	#    that belongs to the logged in user
	#    or get all the projects of that user
	project = profile.project_set.get(id=pk)

	# 4. If there is POST request, process the form,
	#    delete the project, and 
	#    redirect user to projects page
	if request.method == "POST":
		project.delete()
		return redirect('projects:projects')

	# project = Project.objects.get(id=pk)
	# if request.method == "POST":
	# 	project.delete()
	# 	return redirect('projects:projects')
	
	context = {'object':project}
	return render(request, 'projects/delete_template.html', context)

