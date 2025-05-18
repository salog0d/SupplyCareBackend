from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .models import Patient, Diagnosis
from .serializers import PatientSerializer, DiagnosisSerializer


class DiagnosisListCreateView(generics.ListCreateAPIView):
    """
    Handles listing and creating Diagnoses.
    """
    queryset = Diagnosis.objects.all()
    serializer_class = DiagnosisSerializer
    permission_classes = [IsAuthenticated]


class DiagnosisDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles retrieving, updating, and deleting a Diagnosis.
    """
    queryset = Diagnosis.objects.all()
    serializer_class = DiagnosisSerializer
    permission_classes = [IsAuthenticated]


class PatientListCreateView(generics.ListCreateAPIView):
    """
    Handles listing and creating Patients.
    """
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """
        Custom behavior for setting default values during creation.
        """
        serializer.save()


class PatientDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles retrieving, updating, and deleting a Patient.
    """
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]


class PatientByHospitalView(APIView):
    """
    Custom view to get patients by hospital.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, hospital_id):
        patients = Patient.objects.filter(hospital_id=hospital_id)
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
