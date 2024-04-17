from django.urls import path,re_path
from stocks import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('products/', views.ProductListView.as_view(), name='products'),
    path('product/', views.ProductCreationView.as_view(), name='product'),
    path('edit_product/<int:id>/', views.EditProductView.as_view(), name='edit_product'),
    path('delete_product/<int:id>/', views.DeleteProductView.as_view(), name='delete_product'),
    path('product_report/', views.ProductPDFView.as_view(), name='product_report')
]
