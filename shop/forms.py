from django import forms
from .models import CustomerReview

class CommentForm(forms.ModelForm):
    class Meta:
        model = CustomerReview
        fields = ('customer_review',)
     
