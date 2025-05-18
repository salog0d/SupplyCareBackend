from django.db import models
from apps.hospitals.models import Hospital

class MonthlyCompliance(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='compliance')
    month = models.CharField(max_length=20)
    total_orders = models.IntegerField()
    delivered_orders = models.IntegerField()
    compliance_pct = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.hospital.name} - {self.month}"
