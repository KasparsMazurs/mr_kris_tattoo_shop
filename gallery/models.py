import datetime
from django.db import models

class Gallery(models.Model):
    """
    Create a model for galleries
    """
    image = models.ImageField(null=False, blank=False)
    description = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    body_parts = [
        ('Leg', 'Leg'),
        ('Arm', 'Arm'),
        ('Neck', 'Neck'),
        ('Torso', 'Torso'),
        ('Back', 'Back'),
        ('Palm', 'Palm'),
    ]
    body_part = models.CharField(max_length=20, choices=body_parts)
    created_on = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.description
