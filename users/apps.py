"""Apps module for users app"""

from django.apps import AppConfig


class UsersConfig(AppConfig):
    """Class used to configure the users application"""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
