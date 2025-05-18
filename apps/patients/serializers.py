from rest_framework import serializers
from .models import Patient, Diagnosis
from apps.hospitals.serializers import HospitalSerializer
from apps.auth_system.serializers import UserSerializer

class DiagnosisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnosis
        fields = ['id', 'name', 'description']


class PatientSerializer(serializers.ModelSerializer):
    hospital = HospitalSerializer(read_only=True)
    doctor = UserSerializer(read_only=True)
    diagnosis = DiagnosisSerializer(read_only=True)

    class Meta:
        model = Patient
        fields = ['id', 'first_name', 'last_name', 'birthdate', 'location', 'hospital', 'doctor', 'diagnosis', 'is_active', 'registered_at']
