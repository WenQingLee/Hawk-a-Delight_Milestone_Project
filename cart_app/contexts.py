from django.shortcuts import get_object_or_404
from restaurant_app.models import MenuItem


def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering
    every page
    """
    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    item_count = 0
    
    """
    For loop with inputs of id and quantity, to get the item from
    based on the MenuItem model and id and adding the item id, 
    quantity and item to cart_items array.
    """
    for id, quantity in cart.items():
        item = get_object_or_404(MenuItem, pk=id)
        total += quantity * item.price
        item_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'item': item})
    
    return {'cart_items': cart_items, 'total': total, 'item_count': item_count}
