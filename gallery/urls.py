from django.urls import path
from . import views

urlpatterns = [
    path('', views.GalleryListView.as_view(), name='gallery'),
]
