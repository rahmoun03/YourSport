from django.urls import path
from .views import check, sign_up
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('', check),
    path('signup', sign_up),
    path('getTokens', TokenObtainPairView.as_view()),
]