from django.shortcuts import get_object_or_404
from restaurant_app.models import MenuItem


# Store the cart contents and allow it to be available in every page
def cart_contents(request):
    
    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    item_count = 0
    
    
    for id, quantity in cart.items():
        item = get_object_or_404(MenuItem, pk=id)
        
        subtotal = quantity * item.price
        
        total += quantity * item.price
        item_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'item': item, 'subtotal':subtotal})
    
    return {'cart_items': cart_items, 'total': total, 'item_count': item_count}
