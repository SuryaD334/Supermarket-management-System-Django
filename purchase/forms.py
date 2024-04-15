from django import forms
from .models import Purchase

class PurchaseCreationForm(forms.ModelForm):

    class Meta:
        model = Purchase
        fields = ('name', 'description', 'quantity','cost_price', 'current_stock_level','total_stock_level', 'supplier_tel', 'created_by')

class EditPurchaseForm(forms.ModelForm):
   
    class Meta:
        model = Purchase
        fields = ['name', 'description', 'quantity', 'cost_price','current_stock_level','total_stock_level', 'supplier_tel',]
        exclude = ['created_by']
