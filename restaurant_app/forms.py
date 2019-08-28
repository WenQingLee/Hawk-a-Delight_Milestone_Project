from django import forms
from .models import Review

# Form for user submitted reviews for recipes
class RecipeReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ("content", "votes", "image", "published_date")