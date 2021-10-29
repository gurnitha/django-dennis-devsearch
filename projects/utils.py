# projects/utils.py

# Django modules
from django.db.models import Q  
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Locals
from .models import Project, Tag


def paginateProjects(request, projects, results):

	# Step 1: Get the 1st page of the result
	page = request.GET.get('page')
	# Step 2: Use Paginator class with parameter
	#         of Queryset(projects) and the results
	paginator = Paginator(projects, results)

	# Steps 3: If things are ok, use try block
	#          get the first page that contain N results
	try:
		projects = paginator.page(page)

	# Steps 4: If user visited the page for the 1st time,
	#          give him the first page
	except PageNotAnInteger:
		page = 1
		projects = paginator.page(page)

	# Step 5: If no more pages found,
	#         give him the last page
	except EmptyPage:
		page = paginator.num_pages
		projects = paginator.page(page)

	# ----------Customizing the paginator-------------  
	leftIndex = (int(page) - 4)

	if leftIndex < 1:
		leftIndex = 1

	rightIndex = (int(page) + 5)

	if rightIndex > paginator.num_pages:
		rightIndex = paginator.num_pages +1

	custom_range = range(leftIndex, rightIndex)

	# ----------Customizing the paginator-------------  

	return custom_range, projects


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