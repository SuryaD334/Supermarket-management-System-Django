from django.urls import path,re_path
from stocks import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    
    path('product_report/',views.ProductPDFView.as_view(),name='product_report'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
