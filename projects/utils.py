# projects/utils.py

# Django modules
from django.db.models import Q  

# Locals
from .models import Project, Tag


def searchProjects(request):

	# Step 1 Search: search_query with empty string
	search_query = ''

	# Step 2 Search: If there is get request
	if request.GET.get('search_query'):
		search_query = request.GET.get('search_query')

	# # Step 2 Search: Testing search resutl
	# print('SEARCH:', search_query)

	# # Step 3 Search: search by name
	# projects = Project.objects.filter(
	# 	name__icontains=search_query
	# )

	# Step 5 Search: using iexact to search for skills
	tags = Tag.objects.filter(name__icontains=search_query)
	
	# Step 4 Search: using Q look up
	projects = Project.objects.distinct().filter(
		Q(title__icontains=search_query) |
		Q(description__icontains=search_query)|
		Q(owner__name__icontains=search_query)|
		Q(tags__in=tags)
	)
	
	# projects = Project.objects.all()

	return projects, search_query