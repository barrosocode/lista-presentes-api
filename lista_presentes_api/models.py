from django.db import models
from uuid import uuid4

# Convidados
class Convidado(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100, null=False, unique=True)
    confirmed = models.BooleanField(null=False, default=False)

# Presentes
class Presente(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=50, null=False, unique=True)
    image = models.ImageField(upload_to='presentes/', null=True)
    link = models.CharField(max_length=350, null=False)
    store = models.CharField(max_length=50, null=False)
    description = models.TextField(null=False)
    amount = models.IntegerField(null=False, default=1)
    status = models.BooleanField(null=False, default=True)

# Presente_Convidado
class Presente_Convidado(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    presente = models.ForeignKey(Presente, on_delete=models.CASCADE)
    convidado = models.ForeignKey(Convidado, on_delete=models.CASCADE)
