# users/urls.py

# Django modules
from django.urls import path

# Locals
from . import views

# Appname
app_name = 'users'

urlpatterns = [
    path('', views.profiles, name='profiles'),
    path('profile/<str:pk>/', views.userProfile, name='user-profile'),
]
