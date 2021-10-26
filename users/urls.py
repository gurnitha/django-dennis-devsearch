# users/urls.py

# Django modules
from django.urls import path

# Locals
from . import views

# Appname
app_name = 'users'

urlpatterns = [

    # Account
    path('account/', views.userAccount, name='account'),
    path('edit-account/', views.editAccount, name='edit-account'),

    # Authentication
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
    
    # Profiles
    path('', views.profiles, name='profiles'),
    path('profile/<str:pk>/', views.userProfile, name='user-profile'),

    # Skill
    path('create-skill/', views.createSkill, name='create_skill'),
    path('update-skill/<str:pk>/', views.updateSkill, name='update_skill'),
    path('delete-skill/<str:pk>/', views.deleteSkill, name='delete_skill'),
]
