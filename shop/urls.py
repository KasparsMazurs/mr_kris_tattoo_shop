from django.urls import path
from .views import ProductsListView, ProductDetailView

urlpatterns = [
    path('shop/', ProductsListView.as_view(), name='shop'),
    path('product/<slug:slug>/', ProductDetailView.as_view(), name='product-detail'),
]