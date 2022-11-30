from django import forms
from .models import Actuals
 
class ActualsForm(forms.ModelForm):
     class Meta:
         model = Actuals
         fields = '__all__'