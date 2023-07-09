from django.urls import path
from .views import ProductsListView, ProductDetailView
from . import views

urlpatterns = [
    path('shop/', ProductsListView.as_view(), name='shop'),
    path('product/<slug:slug>/', ProductDetailView.as_view(), name='product-detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
]
