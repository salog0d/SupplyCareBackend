from django.urls import path
from .views import (
    MedicineListCreateView, MedicineDetailView,
    InventoryListCreateView, InventoryDetailView
)

urlpatterns = [
    path('medicines/', MedicineListCreateView.as_view(), name='medicine-list'),
    path('medicines/<int:pk>/', MedicineDetailView.as_view(), name='medicine-detail'),
    path('inventory/', InventoryListCreateView.as_view(), name='inventory-list'),
    path('inventory/<int:pk>/', InventoryDetailView.as_view(), name='inventory-detail'),
]
