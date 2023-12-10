"""Apps module for items app"""

from django.apps import AppConfig


class ItemsConfig(AppConfig):
    """Class used to configure the items application"""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'items'
