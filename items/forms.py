"""Forms for the items"""

from django import forms
from .models import Item

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'


class AddItemForm(forms.ModelForm):
    """ Django form class which will be used to add items. """
    class Meta:  # pylint: disable=R0903
        """ Django form class which will be used to add items. """

        model = Item
        fields = ('category', 'name', 'description', 'image', 'price')

        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }


class EditItemForm(forms.ModelForm):
    """ Django form class which will be used to edit stations. """
    class Meta:  # pylint: disable=R0903
        """ Django form class which will be used to edit stations. """

        model = Item
        fields = ('name', 'description', 'image', 'price', 'is_sold')

        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
        }
