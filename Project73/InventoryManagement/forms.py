from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    #Date = forms.DateField(input_formats=['%d-%m-%Y'])
    Date = forms.DateField(label='Date', widget=forms.NumberInput(attrs={'type': 'date'}))

    class Meta:
        model=Product
        fields='__all__'
