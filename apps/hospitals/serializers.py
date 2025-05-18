from rest_framework import serializers
from .models import Hospital, Warehouse

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = ['id', 'name', 'address', 'created_at']


class WarehouseSerializer(serializers.ModelSerializer):
    hospital = HospitalSerializer(read_only=True)

    class Meta:
        model = Warehouse
        fields = ['id', 'name', 'address', 'hospital', 'created_at']
