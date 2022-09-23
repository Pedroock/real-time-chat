from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ValidationError
from django.forms.widgets import PasswordInput, TextInput

class UserCreationForm(UserCreationForm):
    username = forms.CharField(label='Username', min_length=5, max_length=15,
                                widget=TextInput(attrs={'placeholder':'Create an username'}))
    password1 = forms.CharField(label='Password', 
                                widget=PasswordInput(attrs={'placeholder':'Write a password'}))  
    password2 = forms.CharField(label='Confirm password', 
                                widget=PasswordInput(attrs={'placeholder':'Rewrite your password'})) 
    
    def username_clean(self):  
        username = self.cleaned_data['username'].lower()  
        new = User.objects.filter(username = username)  
        if new.count():  
            raise ValidationError("User Already Exist")  
        return username  
    def clean_password2(self):  
        password1 = self.cleaned_data['password1']  
        password2 = self.cleaned_data['password2']  
  
        if password1 and password2 and password1 != password2:  
            raise ValidationError("Password don't match")  
        return password2  

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[str(field)].widget.attrs.update({
                'class': f'{field}'
            })


class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'placeholder': 'Insert your username'}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Insert your password'}))