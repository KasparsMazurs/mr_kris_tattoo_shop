from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_live_51N7ap2Gp1reebzLi5yMeOSPXjpXzmJYVzalcOG3l9ZvPGBGiayNXK9YVu50Nd8vy4POvdx5T7lqEtelNdY8yiCUd00osXlYtDq',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
