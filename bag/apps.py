from django.apps import AppConfig

class BagConfig(AppConfig):
    """
    Configuration class for the 'bag' Django app.
    This will enable the 'bag' app and apply 
    the configuration defined in this class.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bag'
