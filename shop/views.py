from django.shortcuts import render
from django.views.generic import ListView
from .models import Product 

# Create your views here.

class ProductsListView(ListView):
    """
    Will show all Products in shop
    """
    model = Product
    template_name = 'shop.html'
    context_object_name = 'shop_products'

    def get_queryset(self):
        return Product.objects.all()