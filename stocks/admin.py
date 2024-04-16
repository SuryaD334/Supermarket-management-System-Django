from django.contrib import admin
import stocks
from stocks import models

# Register your models here.
admin.register(stocks)
admin.site.register(models.Product)
