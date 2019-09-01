from django.shortcuts import render, redirect, reverse

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
    """
    Gets the cart from the session, which is in contexts.py of
    cart_app. Note that the cart_contents method was added to
    context processes in the hawka_delight_project settings.py 
    so that it is available in all pages during the session
    """
    cart=request.session.get('cart',{})
    cart[id]=cart.get(id, quantity)
    
    request.session['cart']=cart
    return redirect(reverse('index'))
    
def adjust_cart(request, id):
    """
    Used to adjust the quantity of a specified item
    """
    quantity=int(request.POST.get('quantity'))
    cart=request.session.get('cart', {})
    """
    Adjusts the quantity of the item in the cart if it
    is greater than 0. There will be no item if the quantity
    is 0. Otherwise, add the item to cart
    """
    if quantity>0:
        cart[id] = quantity
    else:
        cart.pop(id)
        
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
    
    
    