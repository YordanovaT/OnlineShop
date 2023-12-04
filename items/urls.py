"""Module providing the items app urls."""
from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

app_name = 'item'

urlpatterns = [
    path('<int:pk>/', views.DetailsView.as_view(), name='detail'),
    path('add-item/',views.add_item, name='add-item')
]
