from django.contrib import admin
from .models import Medicine, Inventory

# Register your models here.
admin.site.register(Medicine)
admin.site.register(Inventory)