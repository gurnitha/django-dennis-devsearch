# projects/forms.py

# Django modules
from django.forms import ModelForm, widgets
from django import forms

# Locals
from .models import Project

# Create your forms here.

# Naming the class: ModelName+Form
class ProjectForm(ModelForm):
	class Meta:
		model = Project
		fields = ['title', 'description',
				  'demo_link', 'source_link',
				  'tags']
		# Change multiple select to multiple radion button
		widgets = {'tags': forms.CheckboxSelectMultiple(),}


