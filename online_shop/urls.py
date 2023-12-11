"""Module providing the users app urls."""

from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

app_name = 'shop'  # pylint: disable=C0103

urlpatterns = [
    path('contact/', views.ContactFormView.as_view(), name='contact'),
    path('dashboard/', login_required(views.DashboardView.as_view()), name='dashboard'),
    path('new-conversation/<int:item_id>/',
         login_required(views.new_conversation), name='new-conversation'),
    path('inbox/', login_required(views.inbox), name='inbox'),
    path('<int:conv_id>/', login_required(views.conversation_detail), name='detail'),
    path('', views.IndexView.as_view(), name='base'),
]
