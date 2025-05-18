from django.urls import path
from .views import (
    DiagnosisListCreateView,
    DiagnosisDetailView,
    PatientListCreateView,
    PatientDetailView,
    PatientByHospitalView,
)

urlpatterns = [
    # Diagnosis URLs
    path('diagnoses/', DiagnosisListCreateView.as_view(), name='diagnosis-list-create'),
    path('diagnoses/<int:pk>/', DiagnosisDetailView.as_view(), name='diagnosis-detail'),

    # Patient URLs
    path('patients/', PatientListCreateView.as_view(), name='patient-list-create'),
    path('patients/<int:pk>/', PatientDetailView.as_view(), name='patient-detail'),
    path('patients/hospital/<int:hospital_id>/', PatientByHospitalView.as_view(), name='patients-by-hospital'),
]
