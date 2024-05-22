from django.db import models

# Create your models here.

class NotaFiscal(models.Model):
    numero_nota = models.CharField(max_length=50)
    data_emissao = models.CharField(max_length=50)
    descricao_produtos = models.CharField(max_length=50)
    dados = models.CharField(max_length=50)
    valores = models.CharField(max_length=50)