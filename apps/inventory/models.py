from django.db import models
from django.core.validators import MinValueValidator

class Inventory(models.Model):

    #warehouse = models.ForeignKey('warehouses.Warehouse', on_delete=models.CASCADE, related_name='inventory')
    #medicine = models.ForeignKey('medicines.Medicine', on_delete=models.CASCADE, related_name='inventory')
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    min_threshold = models.IntegerField(validators=[MinValueValidator(0)])
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Inventory - Medicine: {self.medicine.name}, Quantity: {self.quantity}"

    def check_stock(self):
        """Returns True if the quantity is below the minimum threshold."""
        return self.quantity < self.min_threshold
