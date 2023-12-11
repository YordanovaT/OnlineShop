"""Apps module for online_shop app"""

from django.apps import AppConfig


class OnlineShopConfig(AppConfig):
    """Class used to configure the online_shop application"""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'online_shop'
