# users/admin.py

# Django modules
from django.contrib import admin

# Locals
from .models import Profile, Skill

# Register your models here.

admin.site.register(Profile)
admin.site.register(Skill)