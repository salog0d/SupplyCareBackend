from django.db import models

class Hospital(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Warehouse(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='warehouses')
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.hospital.name}"
