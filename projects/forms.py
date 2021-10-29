# projects/forms.py

# Django modules
from django.forms import ModelForm, widgets
from django import forms

# Locals
from .models import Project, Review

# Create your forms here.

# Naming the class: ModelName+Form
class ProjectForm(ModelForm):
	class Meta:
		model = Project
		fields = ['title', 'featured_image', 'description',
				  'demo_link', 'source_link',
				  'tags']
		# Change multiple select to multiple radion button
		widgets = {'tags': forms.CheckboxSelectMultiple(),}

	
	# # Steps adding class style to input fields
	# # 1. Overide the ProjectForm class by
	# #    Define method to modify (add class) to the ProjectForm fields
	def __init__(self, *args, **kwargs):
		super(ProjectForm, self).__init__(*args, **kwargs)

	# 	# 2. Define the field to modify
	# 	self.fields['title'].widget.attrs.update({'class':'input', 'placeholder':'Add title'})
	# 	self.fields['description'].widget.attrs.update({'class':'input', 'placeholder':'Add description'})
	# 	self.fields['demo_link'].widget.attrs.update({'class':'input', 'placeholder':'https://demo.com/my-demo/'})
	# 	self.fields['source_link'].widget.attrs.update({'class':'input', 'placeholder':'https://translate.google.co.id/'})

	# 	# Result

	# 	# BEFORE:

 #  #       <!-- Input:Text -->
 #  #       <div class="form__field">
 #  #           <label 
 #  #               for="formInput#text">Title
 #  #           </label>
 #  #           <input type="text" name="title" maxlength="200" 
 #  #           required id="id_title">
 #  #       </div>

 #  #       AFTER:

 #  #       <!-- Input:Text -->
 #  #       <div class="form__field">
 #  #           <label 
 #  #               for="formInput#text">Title
 #  #           </label>
 #  #           <input type="text" name="title" maxlength="200" 
 #  #           class="input" <<<-- here added
 #  #           placeholder="Add title"  <<<-- here added
 #  #           required id="id_title">
 #  #       </div> 


  # REPLACING THE ABOVE TECHNIQUE USING FOR LOOP

		for name, field in self.fields.items():
			field.widget.attrs.update({'class': 'input'})

		# # RESULT
		# <!-- Input:Text -->
  #       <div class="form__field">
  #           <label 
  #               for="formInput#text">Title
  #           </label>
  #           <input type="text" name="title" maxlength="200" 
  #           class="input" <<<--here added
  #           required id="id_title">
  #       </div>


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value', 'body']

        labels = {
            'value': 'Place your vote',
            'body': 'Add a comment with your vote'
        }

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


