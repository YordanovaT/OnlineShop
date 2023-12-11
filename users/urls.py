"""Module providing the users app urls."""

from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogOutView.as_view(), name='logout'),
    path('activate/<uidb64>/<token>', views.ActivateAccountView.as_view(), name='activate'),
    path('set-new-password/<uidb64>/<token>',
         views.UserSetNewPass.as_view(), name='set-new-password'),
    path('request-password-reset/',
         views.RessetUserPasswordRequest.as_view(), name='request-reset-password')
]
