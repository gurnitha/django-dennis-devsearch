# projects/views.py

# Django modules
from django.shortcuts import render, redirect

# locals
from .models import Project
from .forms import ProjectForm

# Create your views here.

def projects(request):
	projects = Project.objects.all()
	page_title = 'Projects'
	context = {
		'title':page_title,
		'projects':projects
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


def createProject(request):

	# Bring in the ProjectForm class
	form = ProjectForm()

	# If there is POST request, process the form
	if request.method == "POST":

		# Tesing the form: fillin the form and submit it
		# print(request.POST) # tested :)

		# Instantiate the ProjectForm class
		form = ProjectForm(request.POST)
		# Check if form input is valid
		if form.is_valid():
			# Save the input
			form.save()
			return redirect('projects:projects')

	# Context dictionary
	context = {
		'form':form,
	} 

	# Template
	return render(request, 'projects/project_form.html', context)
