from rest_framework import serializers
from .models import MonthlyCompliance
from apps.hospitals.serializers import HospitalSerializer

class MonthlyComplianceSerializer(serializers.ModelSerializer):
    hospital = HospitalSerializer(read_only=True)

    class Meta:
        model = MonthlyCompliance
        fields = ['id', 'hospital', 'month', 'total_orders', 'delivered_orders', 'compliance_pct']
