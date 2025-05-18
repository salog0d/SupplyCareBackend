from django.db import models
from django.core.validators import MinValueValidator
from apps.hospitals.models import Warehouse

class Medicine(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    unit = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Inventory(models.Model):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='inventory')
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE, related_name='inventory')
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    min_threshold = models.IntegerField(validators=[MinValueValidator(0)])
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.medicine.name} - {self.quantity}"
