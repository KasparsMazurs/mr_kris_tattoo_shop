from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    """
    AppConfig for the 'profiles' app.

    Provides the configuration for the 'profiles' app including
    the default auto field and the app name.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'
