"""Module providing the users app urls."""

from django.urls import path, include
from . import views

urlpatterns = [
    path('contact/', views.ContactFormView.as_view(), name='contact'),
    path('', views.IndexView.as_view(), name='base'),
]