from django.views.generic import ListView
from .models import Gallery

# Create your views here.

class GalleryListView(ListView):
    """
    View for displaying all galleries.

    This view retrieves all gallery images from the database
    and displays them in the 'gallery.html' template. It provides
    an option to filter the images by body part using the 'body_part'
    query parameter.
    """
    model = Gallery
    template_name = 'gallery.html'
    context_object_name = 'gallery_images'

    def get_queryset(self):
        """
        Get the queryset for displaying gallery images.

        If a 'body_part' filter is provided in the request's query parameters,
        the queryset will be filtered accordingly. Otherwise, all images will
        be displayed in descending order of their creation date.
        """
        queryset = super().get_queryset()
        body_part_filter = self.request.GET.get('body_part', 'all')
        if body_part_filter == 'all':
            return queryset.order_by('-created_on')  # Newest images first
        else:
            return queryset.filter(body_part=body_part_filter).order_by('-created_on')
        