from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import Recipe, Review
from .forms import RecipeForm, ReviewForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def submit_recipe(request):
    """
    If the submit recipe form is submitted and valid, the form will be saved
    """
    if request.method=="POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipeform = form.save(commit=False)
            recipeform.user = request.user
            recipeform.save()
            messages.success(request, "You have successsfully added a new recipe")
            return redirect(reverse('recipe_list'))
        else:
            return render(request, 'submit-recipe.html', {
                'form' :form
            })
        
            
    """
    Use the form model Recipe form as a template
    """
    form = RecipeForm()
    
    return render(request, "submit-recipe.html", {
        'form' : form
    })
    
# To show all the recipes available
def recipe_list(request):
    recipe_list=Recipe.objects.all()
    
    return render(request, "recipe-list.html", {
        'recipe_list':recipe_list
    })