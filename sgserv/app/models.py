from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE

# Create your models here.
class Endereco(models.Model):
    logradouro = models.CharField(max_length=40)
    numero = models.IntegerField()
    bairro = models.CharField(max_length= 20)
    cidade = models.CharField(max_length= 20)
    uf = models.CharField(max_length= 2)
    cep = models.IntegerField()
    
    def __str__(self):
        return (self.logradouro, self.bairro)

class Cliente(models.Model):
    nome = models.CharField(max_length=30)
    telefone = models.BigIntegerField()
    email = models.EmailField()
    endereco = models.ForeignKey(Endereco, on_delete=CASCADE)
   
    def __str__(self):
        return self.nome
