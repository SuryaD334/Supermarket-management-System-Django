from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic import (CreateView, UpdateView, DeleteView, ListView, DetailView)
from easy_pdf.views import PDFTemplateView
from .forms import ProductCreationForm, EditProductForm
from .models import Product
from .serializers import *
from decorators.decorators import group_required
from helpers.generate_pdf import generate_report
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status, generics


# Create your views here.




