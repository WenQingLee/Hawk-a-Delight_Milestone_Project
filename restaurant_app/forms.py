from django import forms
from .models import review

class RestaurantReviewsForm(forms.ModelForm):
    class Meta:
        model = review
        fields = ("content", "votes")