from django.apps import AppConfig


class ContactmeConfig(AppConfig):
    """
    AppConfig for the 'contactme' app.

    Provides the configuration for the 'contactme' app including
    the default auto field and the app name.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'contactme'
