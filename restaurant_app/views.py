from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Review, MenuItem
from .forms import RecipeReviewForm
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required() 
def get_reviews(request): 
    """
    Create a view that will return the list of reviews 
    that were posted previously and render them to the
    "reviews.html" template
    """
    reviews = Review.objects.filter(published_date__lte=timezone.now()).order_by("-published_date")
    return render(request, "reviews.html", {"reviews":reviews})

def review_detail(request, pk):
    """
    Create a view that returns a single review details based
    on the review id (pk) and render it to the "reviewdetail.html"
    template. Otherwise, return a 404 error if the review is not
    found
    """
    review = get_object_or_404(Review, pk=pk)
    review.views += 1
    review.save()
    return render(request, "reviewdetail.html", {"review":review})
    
def create_edit_review(request, pk=None):
    """
    Create a view that allows us to create or edit a review
    depending on whether the review id is none or not
    """
    review = get_object_or_404(Review, pk=pk) if pk else None
    if request.method == "POST":
        form = RecipeReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            review = form.save()
            return redirect(review_detail, review.pk)
    else:
        form = RecipeReviewForm(instance=review)
        return render(request, "recipereviewform.html", {"form":form})
        
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
    