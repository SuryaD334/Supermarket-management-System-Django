from django import forms
from .models import Company

class CompanyCreationForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('logo','name','address','company_tel','created_by')
        
class CompanyEditForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['logo','name','address','company_tel']
        exclude = ['created_by']