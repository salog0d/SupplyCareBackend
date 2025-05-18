from rest_framework import serializers
from .models import Order, OrderItem, OrderTracking
from apps.auth_system.serializers import UserSerializer
from apps.inventory.serializers import MedicineSerializer

class OrderItemSerializer(serializers.ModelSerializer):
    medicine = MedicineSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'medicine', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    requester = UserSerializer(read_only=True)
    order_items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'requester', 'warehouse', 'created_at', 'status', 'order_items']


class OrderTrackingSerializer(serializers.ModelSerializer):
    order = OrderSerializer(read_only=True)

    class Meta:
        model = OrderTracking
        fields = ['id', 'order', 'status', 'location', 'timestamp']
