"""Module providing the users app urls."""

from django.contrib.auth.decorators import login_required
from django.urls import path, include
from . import views

app_name = 'shop'

urlpatterns = [
    path('contact/', views.ContactFormView.as_view(), name='contact'),
    path('dashboard/', login_required(views.DashboardView.as_view()), name='dashboard'),
    path('', views.IndexView.as_view(), name='base'),
]