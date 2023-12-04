"""Django views module for items app"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from .models import Item
from .forms import AddItemForm, EditItemForm


# Create your views here.

class DetailsView(View):
    """ Class view used for the details functionality """

    def get(self, request, pk):
        """ Method used to GET the details page """
        context = {'has errors': False}
        item = get_object_or_404(Item, pk=pk)
        context['item'] = item

        related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)
        context['related_items'] = related_items

        return render(request, 'items/details.html', context)


def add_item(request):
    """ Method used to add new items """

    context = {'has errors': False}
    # check request
    if request.method == 'POST':
        form = AddItemForm(request.POST, request.FILES)

        # create the new item object but not save it because the 'created_by' is not set yet
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.created_by = request.user
            new_item.save()  # save the item after the 'created_by' field is set

            return redirect('item:detail', pk=new_item.id)

    else:  # the request if GET
        form = AddItemForm()

    form = AddItemForm()
    context['form'] = form
    context['item_title'] = 'New Item'
    return render(request, 'items/add_item.html', context)


def edit_item(request, item_id):
    """ Method used to add new items """

    context = {'has errors': False}
    item = get_object_or_404(Item, pk=item_id, created_by=request.user)
    # check request
    if request.method == 'POST':

        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            context['form'] = form
            form.save()
            return redirect('item:detail', pk=item.id)

        context['form'] = form  # not valid form

    else:  # the request if GET
        form = EditItemForm(instance=item)
        context['form'] = form

    context['item_title'] = 'Edit Item'
    return render(request, 'items/add_item.html', context)


def delete_item(request, item_id):
    """ Method used to delete new items """

    item = get_object_or_404(Item, pk=item_id, created_by=request.user)
    item.delete()

    return redirect('shop:dashboard')
