"""
URL configuration for lista_presentes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
from lista_presentes_api.api import viewsets as apiviewsets

# Creating router
router = routers.DefaultRouter()

# Registering routes
router.register(r'convidados', apiviewsets.ConvidadoViewSet, basename='Convidados')
router.register(r'presentes', apiviewsets.PresenteViewSet, basename='Presentes')
router.register(r'presentes-convidados', apiviewsets.Presente_ConvidadoViewSet, basename='Presentes-Convidados')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
