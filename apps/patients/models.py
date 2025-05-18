from django.db import models
from apps.auth_system.models import User
from apps.hospitals.models import Hospital

class Diagnosis(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField()
    location = models.CharField(max_length=150)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='patients')
    doctor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='patients')
    diagnosis = models.ForeignKey(Diagnosis, on_delete=models.SET_NULL, null=True, related_name='patients')
    is_active = models.BooleanField(default=True)
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
