from django import forms
from .models import ExpenseCategory, Expenses

class CategoryCreationForm(forms.ModelForm):
    class Meta:
        model = ExpenseCategory
        fields = ('name', 'description','created_by')
        

class EditCategoryForm(forms.ModelForm):
    class Meta:
        model = ExpenseCategory
        fields = ['name', 'description']
        exclude = ['created_by']
        
class ExpenseCreationForm(forms.ModelForm):
    class Meta:
        model = Expenses
        fields = ('category', 'description', 'amount', 'created_by')
        
class EditExpenseForm(forms.ModelForm):
    class Meta:
        model = Expenses
        fields = [ 'description', 'amount']
        exclude = ['created_by', 'category']