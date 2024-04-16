from django.urls import path
from company import views as company_views

urlpatterns = [
    path('company/<int:id>/edit/', company_views.CompanyEditView.as_view(), name='company_edit'),
]
