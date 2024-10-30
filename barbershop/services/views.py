from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework import viewsets
from .models import Services
from .serializers import ServicesSerializer

# HTML Görünüşlər (Django CBV)

# Bütün xidmətləri göstərən görünüş
class ServicesListView(ListView):
    model = Services
    template_name = 'services/services_list.html'
    context_object_name = 'services'

# Xüsusi xidməti göstərən görünüş
class ServiceDetailView(DetailView):
    model = Services
    template_name = 'services/service_detail.html'
    context_object_name = 'service'

# Yeni xidmət əlavə etmək
class ServiceCreateView(CreateView):
    model = Services
    fields = ['name', 'description', 'image', 'price', 'salons', 'barbers']
    template_name = 'services/service_form.html'
    success_url = reverse_lazy('services:services_list')

# Xidməti yeniləmək
class ServiceUpdateView(UpdateView):
    model = Services
    fields = ['name', 'description', 'image', 'price', 'salons', 'barbers']
    template_name = 'services/service_form.html'
    success_url = reverse_lazy('services:services_list')

# Xidməti silmək
class ServiceDeleteView(DeleteView):
    model = Services
    template_name = 'services/service_confirm_delete.html'
    success_url = reverse_lazy('services:services_list')


# API Görünüşlər (Django REST Framework)

class ServicesViewset(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
