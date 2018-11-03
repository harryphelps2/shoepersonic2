from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from random import choice
from string import ascii_letters as letters

class UserLoginForm(forms.Form):
    email = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder':'Email'}))
    password = forms.CharField(label="",widget=forms.PasswordInput(attrs={'placeholder':'Password'})) 

    def __init__(self, *args, **kwargs): 
        super(UserLoginForm, self).__init__(*args, **kwargs) 
        self.fields['email'].required = True 
        # remove username
        # self.fields.pop('username')

    def clean(self):
        user = User.objects.get(email=self.cleaned_data.get('email'))
        self.cleaned_data['username'] = user.username
        return super(UserLoginForm, self).clean()

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField()
    email = forms.CharField()
    password1 = forms.CharField(label="Password",widget=forms.PasswordInput) 
    password2 = forms.CharField(label="Retype Password",widget=forms.PasswordInput)  

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
    
    def __init__(self, *args, **kwargs): 
        super(UserRegistrationForm, self).__init__(*args, **kwargs) 
        # remove username
        self.fields.pop('username')

    def save(self):
        random = ''.join([choice(letters) for i in range(30)])
        self.instance.username = random
        return super(UserRegistrationForm, self).save()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'Email address must be unique')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password1 or not password2:
            raise ValidationError("Please confirm your password")
        
        if password1 != password2:
            raise ValidationError("Passwords must match")
        
        return password2