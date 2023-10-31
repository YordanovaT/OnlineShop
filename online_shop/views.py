"""Django views module for online_shop app"""

from django.shortcuts import render, redirect
from django.views.generic import View
from items.models import Category, Item


# Create your views here.


class ContactFormView(View):
    """ Class view used for the contact form functionality """

    def get(self, request):
        """ Method used to GET the contact page """

        return render(request, 'online_shop/contact.html')


class IndexView(View):
    """ Class view used for the index page """

    def get(self, request):
        """ Method used to GET the index page """

        context = {}
        items = Item.objects.filter(is_sold=False)[0:6]
        context['items'] = items
        categories = Category.objects.all()
        context['categories'] = categories

        return render(request, 'users/base.html', context)
