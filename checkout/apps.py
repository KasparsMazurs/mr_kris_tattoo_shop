from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """
    Configuration class for the 'checkout' Django app.
    This will enable the 'checkout' app and apply the configuration defined in this class.

    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

    def ready(self):
        import checkout.signals
