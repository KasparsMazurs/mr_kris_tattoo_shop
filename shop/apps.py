from django.apps import AppConfig


class ShopConfig(AppConfig):
    """
    AppConfig for the 'shop' app.

    Provides the configuration for the 'shop' app including
    the default auto field and the app name.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shop'
