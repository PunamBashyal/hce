from django import forms
from .models import Costomer

class CostomerSignupForm(forms.ModelForm) :
    class Meta:
        model = Costomer
        fields=['name','email','phone','address']
