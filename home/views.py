from django.shortcuts import render

# Create your views here.

def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')

def handling_404(request, exception):
    return render(request, '404.html', {})