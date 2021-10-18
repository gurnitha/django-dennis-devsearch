# projects/views.py

# Django modules
from django.shortcuts import render

# Create your views here.

def projects(request):
	msg = "Message:Learning rendering data to template!"
	msg2 = "Using CONTEXT dictionary"
	context = {
		'message':msg,
		'message2':msg2
	}
	return render(request, 'projects/projects.html', context)


def project(request):
	return render(request, 'projects/single-project.html')