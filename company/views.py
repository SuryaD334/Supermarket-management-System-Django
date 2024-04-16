from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DetailView
from .forms import CompanyEditForm
from .models import Company
from decorators.decorators import group_required

decorators = [group_required(['Admin','Manager','Genral Manager'])]

@method_decorator(decorators, name='dispatch')
class CompanyEditView(UpdateView,DetailView):
    template_name = 'company/company.html'
    pk_url_kwarg = 'id'
    form_class = CompanyEditForm
    queryset = Company.objects.all()
    success_url = reverse_lazy('setting')

