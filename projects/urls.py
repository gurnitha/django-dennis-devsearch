# projects/urls.py

# Django modules
from django.urls import path

# Locals
from . import views

# Appname
app_name = 'projects'

urlpatterns = [
    path('project/', views.projects, name='projects'),
    path('project/<str:pk>/', views.project, name='project'),

    # CRUD
    path('create-project/', views.createProject, name='create-project'),
    path('update-project/<str:pk>/', views.updateProject, name='update-project'),
    path('delete-project/<str:pk>/', views.deleteProject, name='delete-project'),
]
