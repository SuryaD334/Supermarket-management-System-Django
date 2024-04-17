from django.contrib import admin
from .models import Expenses, ExpenseCategory
# Register your models here.

admin.site.register(Expenses)
admin.site.register(ExpenseCategory)
