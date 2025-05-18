
from django.urls import path
from .views import (
    HospitalListCreateView, HospitalDetailView,
    WarehouseListCreateView, WarehouseDetailView
)

urlpatterns = [
    path('hospitals/', HospitalListCreateView.as_view(), name='hospital-list'),
    path('hospitals/<int:pk>/', HospitalDetailView.as_view(), name='hospital-detail'),
    path('warehouses/', WarehouseListCreateView.as_view(), name='warehouse-list'),
    path('warehouses/<int:pk>/', WarehouseDetailView.as_view(), name='warehouse-detail'),
]
