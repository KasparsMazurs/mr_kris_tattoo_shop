from django.urls import path
from . import views

urlpatterns = [
    path('', views.bag, name='bag'),
    path('add/<item_id>/', views.add_to_bag, name='add_to_bag'),
    path('delete/<int:item_id>/', views.delete_from_bag, name='delete_from_bag'),
]