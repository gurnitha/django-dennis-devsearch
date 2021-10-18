# devsearch/urls.py

# Django modules
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # projects
    path('', include('projects.urls', namespace='projects')),
    # admin
    path('admin/', admin.site.urls),
]
