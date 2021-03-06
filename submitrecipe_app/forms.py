from django import forms
from .models import Recipe, Review
from pyuploadcare.dj.forms import ImageField

# Form for user submitted recipes
class RecipeForm(forms.ModelForm):
    image=ImageField(label='Photo')
    class Meta:
        model = Recipe
        fields = ("name", "ingredients", "preparation_steps", "duration", "image")
        
# Form for reviews on recipes
class ReviewForm(forms.ModelForm):
    class Meta:
        labels = {
            'name' : "Review Title"
        }
        model = Review
        fields = ("name", "comment", )