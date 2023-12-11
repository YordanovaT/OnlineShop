"""Models for online shop app"""

from django.db import models
from django.contrib.auth.models import User
from items.models import Item


# Create your models here.


class Conversation(models.Model):
    """ Model class for conversation """

    item = models.ForeignKey(Item, related_name='conversations',  on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:  # pylint: disable=R0903
        """ Class used to show the most recent conversations """

        ordering = ('-modified_at',)

    def __str__(self):
        """Representing the conversations by name, not as objects"""

        return self.item.name


class ConversationMessage(models.Model):
    """ Model class for conversation messages """

    conversation = models.ForeignKey(Conversation,
                                     related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='created_messages', on_delete=models.CASCADE)
