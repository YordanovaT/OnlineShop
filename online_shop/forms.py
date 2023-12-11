"""Forms for conversation"""

from django import forms
from .models import ConversationMessage


class ConversationMessageForm(forms.ModelForm):
    """ Django form class which will be used to have conversations with users. """
    class Meta:  # pylint: disable=R0903
        """ class to configure form for conversations with users. """

        model = ConversationMessage
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={'class': 'w-full py-4 px-6 rounded-xl border'})
        }
