# users/utils.py

# Django modules
from django.db.models import Q  

# Locals
from .models import Profile, Skill 


def searchProfiles(request):

	# Step 1 Search: search_query with empty string
	search_query = ''

	# Step 2 Search: If there is get request
	if request.GET.get('search_query'):
		search_query = request.GET.get('search_query')

	# # Step 2 Search: Testing search resutl
	# print('SEARCH:', search_query)

	# # Step 3 Search: search by name
	# profiles = Profile.objects.filter(
	# 	name__icontains=search_query
	# )

	# Step 5 Search: using iexact to search for skills
	skills = Skill.objects.filter(name__icontains=search_query)
	
	# Step 4 Search: using Q look up
	profiles = Profile.objects.distinct().filter(
		Q(name__icontains=search_query) |
		Q(short_intro__icontains=search_query)|
		Q(skill__in=skills)
	)
	
	# profiles = Profile.objects.all()

	return profiles, search_query