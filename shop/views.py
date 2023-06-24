from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
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
        filter_type = self.request.GET.get('filter')
        if filter_type:
            return Product.objects.filter(product_type=filter_type)
        else:
            return Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_type'] = self.request.GET.get('filter')
        return context

class ProductDetailView(DetailView):
    """
    Show details of a specific product
    """
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'
