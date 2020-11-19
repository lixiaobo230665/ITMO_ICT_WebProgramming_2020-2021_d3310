from django import forms
from .models import Car

class FACForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['state_number', 'Colour', 'Brand', 'Car_type']
