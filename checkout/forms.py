from django import forms
from .models import Order

class ContactDetailsForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('email', 'running_club') 
        exclude = ('first_name', 'last_name', 'address_line_1', 'address_line_2', 'address_line_3', 'town_or_city', 'county', 'postcode')


class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'address_line_1', 'address_line_2', 'address_line_3', 'town_or_city', 'county', 'postcode')
        widgets = {
            'first_name': forms.TextInput(attrs={'autocomplete': 'on'}),
            'last_name': forms.TextInput(attrs={'autocomplete': 'on'}),
            'address_line_1': forms.TextInput(attrs={'autocomplete': 'on'}),
            'address_line_2': forms.TextInput(attrs={'autocomplete': 'on'}),
            'address_line_3': forms.TextInput(attrs={'autocomplete': 'on'}),
            'town_or_city': forms.TextInput(attrs={'autocomplete': 'on'}),
            'county': forms.TextInput(attrs={'autocomplete': 'on'}),
            'postcode': forms.TextInput(attrs={'autocomplete': 'on'}),
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('email', 'running_club','first_name', 'last_name', 'address_line_1', 'address_line_2', 'address_line_3', 'town_or_city', 'county', 'postcode')
