from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import review
from .forms import RecipeReviewForm

# Create your views here.

def show_index(request):
# Create a view for Home page of Hawka-Delight

    return render(request, "base.html")
  
def get_reviews(request): 
    """
    Create a view that will return the reviews that 
    were posted previously and render them to the
    "reviews.html" templat

    