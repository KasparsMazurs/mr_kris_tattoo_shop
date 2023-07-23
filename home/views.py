from django.shortcuts import render


def index(request):
    """
    View for rendering the index page.

    This view returns the 'index.html' template to render
    the index page.
    """
    return render(request, 'home/index.html')


def handling_404(request, exception):
    """
    View for handling the 404 page not found error.

    This view returns the '404.html' template to render the
    custom 404 page.
    """
    return render(request, '404.html', {})
