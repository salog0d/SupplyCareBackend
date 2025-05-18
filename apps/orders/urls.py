from django.urls import path
from .views import (
    OrderListCreateView, OrderDetailView,
    OrderItemListCreateView, OrderItemDetailView,
    OrderTrackingListCreateView, OrderTrackingDetailView,
    OrdersByWarehouseView
)

urlpatterns = [
    path('orders/', OrderListCreateView.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('order-items/', OrderItemListCreateView.as_view(), name='orderitem-list'),
    path('order-items/<int:pk>/', OrderItemDetailView.as_view(), name='orderitem-detail'),
    path('order-tracking/', OrderTrackingListCreateView.as_view(), name='ordertracking-list'),
    path('order-tracking/<int:pk>/', OrderTrackingDetailView.as_view(), name='ordertracking-detail'),
    path('orders/warehouse/<int:warehouse_id>/', OrdersByWarehouseView.as_view(), name='orders-by-warehouse'),
]
