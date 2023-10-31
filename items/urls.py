"""Module providing the items app urls."""
from django.urls import path
from . import views

app_name = 'item'

urlpatterns = [
    path('<int:pk>/', views.DetailsView.as_view(), name='detail'),
]
