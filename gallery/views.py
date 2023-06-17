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
        queryset = super().get_queryset()
        body_part_filter = self.request.GET.get('body_part', 'all')
        if body_part_filter == 'all':
            return queryset.order_by('-created_on')  # Newest images first
        else:
            return queryset.filter(body_part=body_part_filter).order_by('-created_on')