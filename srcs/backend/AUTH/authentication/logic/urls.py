from django.urls import path
from .views import register, login

urlpatterns = [
    path('sign_up', register),
    path('sign_in', login),
]