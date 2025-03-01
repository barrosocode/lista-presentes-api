from rest_framework import viewsets
from lista_presentes_api.api import serializers
from lista_presentes_api import models

# Convidados
class ConvidadoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ConvidadosSerializer
    queryset = models.Convidado.objects.all()

# Presentes
class PresenteViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PresentesSerializer
    queryset = models.Presente.objects.all()

# Presentes_Convidados
class Presente_ConvidadoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.Presentes_ConvidadosSerializer
    queryset = models.Presente_Convidado.objects.all()
