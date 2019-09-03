from django.shortcuts import render
from restaurant_app.models import MenuItem

# Create your views here.

def do_search(request):
    item=MenuItem.objects.filter(name__icontains=request.GET['query'])
    return render(request, "menu-items.html", {'all_menu_items':item})