from django.db import models

# Create your models here.

class Comment(models.Model):
    """
    Create a model for comments
    """
    post = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='product_comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

class Product(models.Model):
    """
    Create a model for products
    """
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    product_price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    types = [
        ('Black and white drawing', 'Black and white drawing'),
        ('Colourful drawing', 'Colourful drawing'),
        ('Painting', 'Painting'),
    ]
    product_type = models.CharField(max_length=40, choices=types, default='Black and white drawing')

    def __str__(self):
        return self.name