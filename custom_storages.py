from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    """
    Custom storage class for static files.

    This class extends the S3Boto3Storage class provided by the
    `django-storages` library and sets the location to the staticfiles
    location specified in the settings.
    """

    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    """
    Custom storage class for media files.

    This class extends the S3Boto3Storage class provided by the
    `django-storages` library and sets the location to the mediafiles
    location specified in the settings.
    """

    location = settings.MEDIAFILES_LOCATION
