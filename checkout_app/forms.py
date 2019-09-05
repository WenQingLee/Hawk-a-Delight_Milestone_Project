from django import forms
from .models import Order

# Allows the user to key in their credit card information for validation
class MakePaymentForm(forms.Form):
    
    MONTH_CHOICES = [(i, i) for i in range(1,13)]
    YEAR_CHOICES = [(i, i) for i in range (2019, 2040)]
    
    credit_card_number = forms.CharField(label='Credit card number', required=False)
    cvv = forms.CharField(label='Security Code (CVV)', required=False)
    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)

# Additional information for the user to fill up during payment    
class OrderForm(forms.ModelForm):
    
    class Meta:
        labels = {
            'postcode' : "Postal Code",
            'street_address1' : "Street Address 1",
            'street_address2' : "Street Address 2",
        }
        model = Order
        fields = ('full_name', 'phone_number', 'country', 'postcode', 'town_or_city', 'street_address1', 'street_address2')
        