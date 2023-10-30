"""Django views module"""

from django.shortcuts import render, redirect
from django.views.generic import View


# Create your views here.


class ContactFormView(View):
    """
        Class view used for the registration functionality
        """

    def get(self, request):
        """ Method used to GET the register page """

        return render(request, 'online_shop/contact.html')


class IndexView(View):
    """
        Class view used for the registration functionality
        """

    def get(self, request):
        """ Method used to GET the register page """

        return render(request, 'users/base.html')
