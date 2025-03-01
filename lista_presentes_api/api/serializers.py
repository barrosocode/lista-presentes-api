from rest_framework import serializers
from lista_presentes_api import models

# Convidados Serializer
class ConvidadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Convidado
        fields = '__all__'

# Presentes Serializer
class PresentesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Presente
        fields = '__all__'

# Presentes_Convidados Serializer
class Presentes_ConvidadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Presente_Convidado
        fields = '__all__'
