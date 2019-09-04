from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import MenuItem
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required()
def all_menu_items(request):
    all_menu_items = MenuItem.objects.all().order_by('name')
    return render(request, 'menu-items.html', {'all_menu_items':all_menu_items})
    
@login_required()
def menu_item_detail(request, pk):
    menu_item_detail = get_object_or_404(MenuItem, pk=pk)
    return render(request, "menu-item-detail.html", {
        'menu_item_detail':menu_item_detail
    })
    
@login_required()
def menu_type(request, type):
    
    if type == "Breakfast":
        menu_item_type = MenuItem.objects.filter(type="Breakfast")
    elif type == "Lunch":
        menu_item_type = MenuItem.objects.filter(type="Lunch")
    elif type == "Dinner":
        menu_item_type = MenuItem.objects.filter(type="Dinner")
        
    return render(request, "menu-items.html",{
        'all_menu_items': menu_item_type
    })
        
    