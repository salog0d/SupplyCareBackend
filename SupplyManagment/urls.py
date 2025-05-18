"""
URL configuration for SupplyManagment project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('apps.auth_system.urls')),
    path('api/v1/hospitals/', include('apps.hospitals.urls')),
    path('api/v1/inventory/', include('apps.inventory.urls')),
    path('api/v1/orders/', include('apps.orders.urls')),
    path('api/v1/compliance/', include('apps.compilance.urls')),
    path('api/v1/patients/', include('apps.patients.urls')),
]
