# projects/admin.py

# Django modules
from django.contrib import admin

# Loclas
from projects.models import Project

# Register your models here.
admin.site.register(Project)