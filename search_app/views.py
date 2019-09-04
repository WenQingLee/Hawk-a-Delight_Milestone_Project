from django.shortcuts import render
from restaurant_app.models import MenuItem
from submitrecipe_app.models import Recipe

# Create your views here.

def do_menu_search(request):
    item=MenuItem.objects.filter(name__icontains=request.GET['query'])
    return render(request, "menu-items.html", {'all_menu_items':item})
    
def do_recipe_search(request):
    recipe=Recipe.objects.filter(name__icontains=request.GET['query'])
    return render(request, "recipe-list.html", {'recipe_list':recipe})