from django.contrib import admin
from .models import Diagnosis, Patient

# Register your models here.
admin.site.register(Diagnosis)
admin.site.register(Patient)