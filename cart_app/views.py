from django.shortcuts import render, redirect, reverse
from django.contrib import messages

# Create your views here.

def view_cart(request):
    # A view that renders the cart contents page
    return render(request, "cart.html")
    
def add_to_cart(request, id):
    """
    Add a quantity of the specified item to cart from the input
    name, quantity, of menu-item.html in restaurant_app
    """
    quantity=int(request.POST.get('quantity'))

    cart=request.session.get('cart',{})
    cart[id]=cart.get(id, quantity)
    
    request.session['cart']=cart
    
    messages.success(request, "You have successsfully added the dish to your cart")
    
    return redirect(reverse('all_menu_items'))
    
def adjust_cart(request, id):
    """
    Used to adjust the quantity of a specified item
    """
    quantity=int(request.POST.get('quantity'))
    cart=request.session.get('cart', {})
    """
    Adjusts the quantity of the item in the cart according to the property, id,
    if it is greater than 0. There will be no item if the quantity
    is 0 as it will be removed from the array. Note that id has to be converted
    to a string as it was defined as an integer in the urls.py
    """
    if quantity>0:
        cart[id] = quantity
    else:
        cart.pop(str(id))
        
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
    
    
    