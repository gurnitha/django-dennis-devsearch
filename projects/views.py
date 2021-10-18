# projects/views.py

# Django modules
from django.shortcuts import render

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
	form = ProjectForm()
	context = {
		'form':form,
	} 
	return render(request, 'projects/project_form.html', context)
