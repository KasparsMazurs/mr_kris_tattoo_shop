from django.apps import AppConfig


class GalleryConfig(AppConfig):
    """
    AppConfig for the 'gallery' app.

    Provides the configuration for the 'gallery' app including
    the default auto field and the app name.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gallery'
