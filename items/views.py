"""Django views module for items app"""

from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import Item


# Create your views here.

class DetailsView(View):
    """ Class view used for the details functionality """
    def get(self, request, pk):
        """ Method used to GET the details page """
        context = {'has errors': False}
        item = get_object_or_404(Item, pk=pk)
        context['item'] = item

        related_items=Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)
        context['related_items'] = related_items

        return render(request, 'items/details.html', context)
