from django.db import models

# Create your models here.

class Funcionarios(models.Model):
    competencia = models.CharField(max_length=50)
    habilidades = models.CharField(max_length=50)
    responsabilidade = models.CharField(max_length=50)
    adaptabilidade = models.CharField(max_length=50)
    etica = models.CharField(max_length=50)