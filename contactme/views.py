from django.shortcuts import render

# Create your views here.

def contactme(request):
    """ A view to return the contactme page """

    return render(request, 'contactme.html')

def thank_you(request):
    """ A view to return the thank_you page """

    return render(request, 'thank_you.html')