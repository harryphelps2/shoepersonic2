from django import forms
from .models import Order

class ContactDetailsForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('email', 'running_club') 
        widgets = {
            'email': forms.TextInput(attrs={
                'autocomplete': 'on',
                'placeholder' : 'Email Address (required)'
                }),
            'running_club': forms.TextInput(attrs={
                'autocomplete': 'on',
                'placeholder' : 'Running Club'
                }),
        }

class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'address_line_1', 'address_line_2', 'address_line_3', 'town_or_city', 'county', 'postcode')
        widgets = {
            'first_name': forms.TextInput(attrs={
                'autocomplete' : 'on',
                'placeholder' : 'First Name (required)'}),
            'last_name': forms.TextInput(attrs={
                'autocomplete' : 'on',
                'placeholder' : 'Last Name (required)'}),
            'address_line_1': forms.TextInput(attrs={
                'autocomplete' : 'on',
                'placeholder' : 'Address Line 1 (required)'}),
            'address_line_2': forms.TextInput(attrs={
                'autocomplete' : 'on',
                'placeholder' : 'Address Line 2'}),
            'address_line_3': forms.TextInput(attrs={
                'autocomplete' : 'on',
                'placeholder' : 'Address Line 3'}),
            'town_or_city': forms.TextInput(attrs={
                'autocomplete' : 'on',
                'placeholder' : 'Town or City'}),
            'county': forms.TextInput(attrs={
                'autocomplete' : 'on',
                'placeholder' : 'County'}),
            'postcode': forms.TextInput(attrs={
                'autocomplete' : 'on',
                'placeholder' : 'Postcode (required)'}),
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('email', 'running_club','first_name', 'last_name', 'address_line_1', 'address_line_2', 'address_line_3', 'town_or_city', 'county', 'postcode')
