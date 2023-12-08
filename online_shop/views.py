"""Django views module for online_shop app"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import View
from items.models import Category, Item
from .models import Conversation
from .forms import ConversationMessageForm


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


class DashboardView(View):
    """ Class view used for the index page """

    def get(self, request):
        context = {}
        items = Item.objects.filter(created_by=request.user)

        context['items'] = items
        return render(request, 'online_shop/dashboard.html', context)


def new_conversation(request, item_id):
    """ View used for starting conversation with seller regarding an item """
    context = {}

    item = get_object_or_404(Item, pk=item_id)

    if item.created_by == request.user:
        return render(request, 'online_shop/new_conversation.html', context, status=400)

    # all conversions the user is member of
    conversation = Conversation.objects.filter(item=item).filter(members__in=[request.user.id])

    if conversation:  # if there are conversations
        return redirect('shop:detail', pk=conversation.first().id)
    if request.method == 'POST':

        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            messages.add_message(request, messages.SUCCESS,
                                 ' You successfully sent message.')

            return redirect('item:detail', pk=item_id)
    else:
        form = ConversationMessageForm()
    context['form'] = form
    return render(request, 'online_shop/new_conversation.html', context)


def inbox(request):
    """ View used for showing all conversation messages received """
    conversations = Conversation.objects.filter(members__in=[request.user.id])
    context = {'conversations': conversations}

    return render(request, 'online_shop/inbox.html', context)


def conversation_detail(request, pk):
    """ View used for showing conversation details """

    conversation = Conversation.objects.filter(members__in=[request.user.id]).get(pk=pk)

    context = {'conversation': conversation}
    if request.method == 'POST':

        form = ConversationMessageForm(request.POST)

        if form.is_valid():

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            conversation.save()

            return redirect('shop:detail', pk=pk)
    else:
        form = ConversationMessageForm()
    context['form'] = form
    return render(request, 'online_shop/detail.html', context)
