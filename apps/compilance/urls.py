from django.urls import path
from .views import (
    ComplianceListCreateView,ComplianceDetailView
)

urlpatterns = [
    path('compliance/', ComplianceListCreateView.as_view(), name='compliance-list'),
    path('compliance/<int:pk>/', ComplianceDetailView.as_view(), name='compliance-detail'),
]
