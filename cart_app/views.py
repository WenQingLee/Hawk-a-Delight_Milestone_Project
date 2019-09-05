from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

# Allows the user to check the contents of their cart
@login_required()
def view_cart(request):
    return render(request, "cart.html")
    
# Allows the user to add the menu item to their cart
@login_required()
def add_to_cart(request, id):
    
    if request.POST.get('quantity') != "":
    
        quantity=int(request.POST.get('quantity'))
    
        cart=request.session.get('cart',{})
        cart[id]=cart.get(id, quantity)
        
        request.session['cart']=cart
        
        messages.success(request, "You have successsfully added the dish to your cart")
        
        return redirect(reverse('menu_item_detail' , kwargs={'pk':id} ))
    
    messages.success(request, "Please provide a value from 0 to 99 for the quantity of the dish")
    
    return redirect(reverse('menu_item_detail' , kwargs={'pk':id} ))

# Allows the user to edit the quantity of menu item in their cart after adding
@login_required()
def adjust_cart(request, id):
    
        if request.POST.get('quantity') != "":
            
            quantity=int(request.POST.get('quantity'))
            cart=request.session.get('cart', {})
        
            if quantity>0:
                cart[id] = quantity
            else:
                cart.pop(str(id))
                
            request.session['cart'] = cart
            
            return redirect(reverse('view_cart'))
            
        messages.success(request, "Please provide a value from 0 to 99 for the quantity of the dish")
        
        return redirect(reverse('view_cart'))
    
    
    