# users/admin.py

# Django modules
from django.contrib import admin

# Locals
from .models import Profile

# Register your models here.

admin.site.register(Profile)