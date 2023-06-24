from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.http import require_POST
from django.http import JsonResponse

# Create your views here.
def bag(request):
    """ A view to return the shoping bag page """

    return render(request, 'bag.html')

def add_to_bag(request, item_id):
    """ Add a specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)

@require_POST
def delete_from_bag(request, item_id):
    # Retrieve the product item from the shopping bag and set the quantity to 0
    bag = request.session.get('bag', {})
    bag[item_id] = 0
    request.session['bag'] = bag

    # Return a JSON response to indicate the successful deletion
    return JsonResponse({'message': 'Product deleted from cart'})