from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name','address_line_1', 'address_line_2', 'address_line_3', 'town_or_city', 'county', 'postcode')
