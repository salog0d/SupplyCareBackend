from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import MonthlyCompliance
from .serializers import MonthlyComplianceSerializer

class ComplianceListCreateView(generics.ListCreateAPIView):
    queryset = MonthlyCompliance.objects.all()
    serializer_class = MonthlyComplianceSerializer
    permission_classes = [IsAuthenticated]


class ComplianceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MonthlyCompliance.objects.all()
    serializer_class = MonthlyComplianceSerializer
    permission_classes = [IsAuthenticated]
