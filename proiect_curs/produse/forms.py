from django import forms

from .models import Products


class ProductsForm(forms.ModelForm):
    product = forms.CharField(label='Produs', max_length=100)
    stoc_disponibil = forms.IntegerField(label='Stocul produsului')
    #product1 = forms.CharField(label='Produs1', max_length=100)
    #product2 = forms.CharField(label='Produs2', max_length=100)
    #product3 = forms.CharField(label='Produs3', max_length=100)
    class Meta:
      model = Products
      fields = ['product' ,'stoc_disponibil']
