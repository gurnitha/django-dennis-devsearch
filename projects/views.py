# projects/views.py

# Django modules
from django.shortcuts import render

# Create your views here.

def projects(request):
	msg = "Message:Learning rendering data to template!"
	return render(request, 'projects/projects.html', {'message':msg})


def project(request):
	return render(request, 'projects/single-project.html')