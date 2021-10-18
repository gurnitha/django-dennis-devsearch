# projects/urls.py

# Django modules
from django.urls import path

# Locals
from . import views

# Appname
app_name = 'projects'

urlpatterns = [
    path('projects/', views.projects, name='projects'),
    path('project/', views.project, name='project'),
]
