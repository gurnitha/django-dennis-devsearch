# projects/admin.py

# Django modules
from django.contrib import admin

# Loclas
from projects.models import Project, Review

# Register your models here.
admin.site.register(Project)
admin.site.register(Review)