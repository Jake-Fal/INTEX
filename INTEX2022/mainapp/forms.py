from django import forms
# from .models import Login
from django.contrib.auth.models import User
 
class LoginForm(forms.ModelForm):
     class Meta:
         model = User
         fields = ('username', 'password')

        