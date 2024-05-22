from django.db import models

# Create your models here.

class Produtos(models.Model):
    preco = models.CharField(max_length=50)
    qualidades = models.CharField(max_length=50)
    funcionalidades = models.CharField(max_length=50)
    desing = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)