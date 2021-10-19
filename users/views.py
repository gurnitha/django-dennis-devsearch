# users/views.py

# Django modules
from django.shortcuts import render

# Create your views here.

# Profile view
def profiles(request):
	return render(request, 'users/profiles.html')