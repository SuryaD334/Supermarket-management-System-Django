from django import forms
from sales.models import Sales

class SalesCreationForm(forms.Modelform):
    
    class Meta:
        model = Sales
        fields = ('name','item', 'quantity', 'unit_price', 'total_amount', 'sold_by')
        
    def save(self, commit = True):
        sale = super(SalesCreationForm,self).save(commit = False)
        
        if commit:
            sale.name = self.cleaned_data.get('name')
            sale.unit_price = self.cleaned_data.get('unit_price')
            sale.total_amount = self.cleaned_data.get('total_amount')
            sale.sold_by = self.cleaned_data.get('sold_by')
            sale.save()
        return sale
        
class SalesEditForm(forms.ModelForm):
    
    class Meta:
        model = Sales
        fields = ['item', 'quantity']
