from django.db import models

# Create your models here.

class Fornecedores(models.Model):
    qualidade = models.CharField(max_length=50)
    capacidade = models.CharField(max_length=50)
    custo = models.CharField(max_length=50)
    reputacao = models.CharField(max_length=50)
    suporte = models.CharField(max_length=50)