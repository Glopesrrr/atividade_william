from django.db import models

# Create your models here.

class Clientes(models.Model):
    necessidade = models.CharField(max_length=50)
    comportamento = models.CharField(max_length=50)
    feedback = models.CharField(max_length=50)
    potencial = models.CharField(max_length=50)
    demografia = models.CharField(max_length=50)