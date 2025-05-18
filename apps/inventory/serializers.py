from rest_framework import serializers
from .models import Medicine, Inventory
from apps.hospitals.serializers import WarehouseSerializer

class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = ['id', 'name', 'description', 'unit']


class InventorySerializer(serializers.ModelSerializer):
    warehouse = WarehouseSerializer(read_only=True)
    medicine = MedicineSerializer(read_only=True)

    class Meta:
        model = Inventory
        fields = ['id', 'warehouse', 'medicine', 'quantity', 'min_threshold', 'updated_at']
