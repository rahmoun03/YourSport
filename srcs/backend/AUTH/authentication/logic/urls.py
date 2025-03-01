from django.urls import path
from .views import register, login, get_profile_data

urlpatterns = [
    path('sign_up', register),
    path('sign_in', login),
    path('profile', get_profile_data),
]