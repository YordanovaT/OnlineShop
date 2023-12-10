"""Module providing the items app urls."""
from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

app_name = 'item'  # pylint: disable=C0103

urlpatterns = [
    path('<int:item_id>/', views.DetailsView.as_view(), name='detail'),
    path('add-item/', login_required(views.add_item), name='add-item'),
    path('<int:item_id>/edit/', login_required(views.edit_item), name='edit'),
    path('<int:item_id>/delete/', login_required(views.delete_item), name='delete'),
    path('browse/', views.list_items_by_category, name='browse_by_category'),
    path('', views.browse_items, name='browse_items')
]
