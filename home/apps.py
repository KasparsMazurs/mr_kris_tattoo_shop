from django.apps import AppConfig


class HomeConfig(AppConfig):
    """
    AppConfig for the 'home' app.

    Provides the configuration for the 'home' app including
    the default auto field and the app name.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
