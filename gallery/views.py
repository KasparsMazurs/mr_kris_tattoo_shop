from django.shortcuts import render
from django.views.generic import ListView
from .models import Gallery 

# Create your views here.

class GalleryListView(ListView):
    """
    Will show all galleries
    """
    model = Gallery
    template_name = 'gallery.html'
    context_object_name = 'gallery_images'

    def get_queryset(self):
        return super().get_queryset()