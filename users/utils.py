# users/utils.py

# Django modules
from django.db.models import Q  

# Locals
from .models import Profile, Skill 
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


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


def paginateProfiles(request, profiles, results):

	# Step 1: Get the 1st page of the result
	page = request.GET.get('page')
	# Step 2: Use Paginator class with parameter
	#         of Queryset(profiles) and the results
	paginator = Paginator(profiles, results)

	# Steps 3: If things are ok, use try block
	#          get the first page that contain N results
	try:
		profiles = paginator.page(page)

	# Steps 4: If user visited the page for the 1st time,
	#          give him the first page
	except PageNotAnInteger:
		page = 1
		profiles = paginator.page(page)

	# Step 5: If no more pages found,
	#         give him the last page
	except EmptyPage:
		page = paginator.num_pages
		profiles = paginator.page(page)

	# ----------Customizing the paginator-------------  
	leftIndex = (int(page) - 4)

	if leftIndex < 1:
		leftIndex = 1

	rightIndex = (int(page) + 5)

	if rightIndex > paginator.num_pages:
		rightIndex = paginator.num_pages +1

	custom_range = range(leftIndex, rightIndex)

	# ----------Customizing the paginator-------------  

	return custom_range, profiles
