from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Recipe, Review
from .forms import RecipeForm, ReviewForm
from django.contrib.auth.decorators import login_required

# Create your views here.

# To allow users to submit a recipe
@login_required()
def submit_recipe(request):
    """
    If the submit recipe form is submitted and valid, the form will be saved
    """
    if request.method=="POST":
        form = RecipeForm(request.POST, request.FILES)
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
    recipe_list=Recipe.objects.all().order_by('-created_date')
    
    return render(request, "recipe-list.html", {
        'recipe_list':recipe_list,
    })

# To return the recipe details based on the recipe ID(pk)
def recipe_details(request, id):
    recipe = get_object_or_404(Recipe, pk=id)
    reviews = recipe.review_set.all()
    recipe.views += 1
    
    recipe.save()
    return render(request, "recipe-detail.html", {
        'recipe':recipe,
        'recipe_review':reviews,
    })

# To allo users to submit reviews for the recipes
@login_required()
def submit_review(request, id):
    """
    If the submit review form is submitted and valid, the form will be saved
    """
    if request.method=="POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            recipe = get_object_or_404(Recipe, pk=id)
            reviewform = form.save(commit=False)
            reviewform.user = request.user
            reviewform.recipe = recipe
            reviewform.save()
            messages.success(request, "You have successfully submitted a review")
            return redirect(reverse('recipe_details', kwargs={'id':id} ))
        else:
            return render(request, 'submit-review.html', {
                'form' : form,
                'recipe':recipe,
            })
            
    form = ReviewForm()
    
    return render(request, "submit-review.html", {
        'form' : form
    })

# To allow the users to upvote the recipes
@login_required()
def upvote_recipe(request, id):
    recipe = get_object_or_404(Recipe, pk=id)
    recipe.votes +=1
    recipe.save()
    return render(request, "recipe-detail.html", {
        'recipe':recipe,
    })
    
# To allow the user to edit their submitted recipes
@login_required()
def edit_recipe(request, id):
    recipe = get_object_or_404(Recipe, pk=id)
    
    if request.method=="POST":
        form=RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            recipeform = form.save(commit=False)
            recipeform.user = request.user
            recipeform.save()
            messages.success(request, "You have successsfully updated the recipe")
            return redirect(reverse('recipe_details', kwargs={'id':id} ))
        else:
            return render(request, 'edit-recipe.html', {
                'form':form,
                'recipe':recipe,
            })
            
    form = RecipeForm()
    
    return render(request, "edit-recipe.html",{
        'form' : form
    })
    
# To allow the user to edit their submitted reviews    
@login_required()
def edit_review(request, id):
    
    if request.method=="POST":
        review=get_object_or_404(Review, pk=id)
        form=ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            reviewform=form.save(commit=False)
            reviewform.user = request.user
            reviewform.recipe = review.recipe
            reviewform.save()
            messages.success(request, "You have successfully submitted a review")
            return redirect(reverse('recipe_details', kwargs={'id':id} ))
        else:
            return render(request, "edit-review.html",{
                'form':form,
            })
            
    form = ReviewForm()
    
    return render(request, "edit-review.html", {
        'form' : form
    })
        