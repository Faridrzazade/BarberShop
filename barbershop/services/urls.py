from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ServicesListView, ServiceDetailView, ServiceCreateView,
    ServiceUpdateView, ServiceDeleteView, ServicesViewset
)

# REST Framework router-i üçün
router = DefaultRouter()
router.register(r'services', ServicesViewset)

app_name = 'services'

urlpatterns = [
    path('', ServicesListView.as_view(), name='services_list'),
    path('service/<int:pk>/', ServiceDetailView.as_view(), name='service_detail'),
    path('service/new/', ServiceCreateView.as_view(), name='service_create'),
    path('service/<int:pk>/edit/', ServiceUpdateView.as_view(), name='service_update'),
    path('service/<int:pk>/delete/', ServiceDeleteView.as_view(), name='service_delete'),
    path('api/', include(router.urls)),  # API görünüşlər üçün
]
