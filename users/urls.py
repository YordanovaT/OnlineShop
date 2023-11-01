"""Module providing the users app urls."""

from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
]