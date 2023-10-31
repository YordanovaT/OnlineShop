"""Models for the items app"""

from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Category(models.Model):
    """Model class for the item categories"""
    name = models.CharField(max_length=150)

    class Meta:
        """
        Creating class to show categories as plural and to order them by name
        """

        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        """Representing the categories by name, not as objects"""

        return self.name


class Item(models.Model):
    """Model class for the items"""

    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()  # add validation for min and max price
    is_sold = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)

    def __str__(self):
        """Representing the items by name, not as objects"""

        return self.name
