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
        return (self.logradouro)

class Cliente(models.Model):

    NATUREZA_CHOICES = [
        ('0', 'Pessoa Física'),
        ('1', 'Pessoa Jurídica'),
    ]
    SITUACAO_CHOICES = [ 
        ('0', 'Ativo'),
        ('1', 'Inativo'),
        ('2', 'Bloqueado'),
    ]
    nome = models.CharField(max_length=30)
    natureza = models.CharField(max_length=1, choices= NATUREZA_CHOICES)
    cadastro_fiscal = models.CharField(max_length=16, default="0000000000000000")
    telefone = models.CharField(max_length= 14)
    email = models.EmailField()
    endereco = models.ForeignKey(Endereco, on_delete=CASCADE)
    data_cadastro = models.DateField()
    situacao = models.CharField(max_length=1, choices= SITUACAO_CHOICES)
   
    def __str__(self):
        return self.nome

class Fornecedor(models.Model):
    nome = models.CharField(max_length=50)
    CNPJ = models.BigIntegerField()
    telefone = models.BigIntegerField()
    email = models.EmailField()
    endereco = models.ForeignKey(Endereco, on_delete=CASCADE)

    def __str__(self):
        return self.nome

class Equipamentos(models.Model):
    CAPACIDADE_CHOICES = [
        ('0', '127V'),
        ('1', '220V'),
    ]
    nome = models.CharField(max_length= 30)
    marca = models.CharField(max_length= 20)
    modelo = models.CharField(max_length= 20)
    serie = models.IntegerField()
    capacidade = models.CharField(max_length= 6, choices= CAPACIDADE_CHOICES)

    def __str__(self):
        return self.nome

class Insumos(models.Model):


    def __str__(self):
        return self

class Compromisso(models.Model):
    TIPO_SOLICITACAO_CHOICES = [
        ('0', 'Visita técnica'),
        ('1', 'Reparo em portões'),
        ('2', 'Reparo em rede elétrica'),
        ('3', 'Instalação de câmeras'),
    ]
    SITUACAO_CHOICES = [ 
        ('0', 'A iniciar'),
        ('1', 'Em andamento'),
        ('2', 'Encerrada'),
    ]
    id = id
    data = models.DateField()   
    hora = models.TimeField()
    tipo = models.CharField(max_length= 30, choices=TIPO_SOLICITACAO_CHOICES)
    descricao = models.TextField()
    cliente = models.ForeignKey(Cliente, on_delete=CASCADE)
    equipamentos = models.ManyToManyField(Equipamentos)
    situacao = models.CharField(default= ('0', 'A iniciar'), max_length= 30, choices= SITUACAO_CHOICES)

    def __str__(self):
        return self.tipo

class NotaFiscal(models.Model):
    TIPO_NOTAFISCAL_CHOICES = [ 
        ('0', 'Entrada'),
        ('1', 'Saída'),
    ]
    numero = models.BigIntegerField()
    tipo = models.CharField(max_length= 10, choices= TIPO_NOTAFISCAL_CHOICES)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=CASCADE)
    valor = models.FloatField()

    def __str__(self):
        return str(self.numero)
    

class ContasaPagar(models.Model):
    SITUACAO_BOLETO_CHOICES = [
        ('1', 'A vencer'),
        ('2', 'Vencido'),
        ('3', 'Protestado'),
        ('4', 'Pago até o vencimento'),
        ('5', 'Regularizado'),
    ]
    vencimento = models.DateField()
    valor = models.FloatField()
    fornecedor = models.ForeignKey(Fornecedor, on_delete=CASCADE)
    situacao = models.CharField(
        max_length=25,
        choices=SITUACAO_BOLETO_CHOICES,
        default= '1')
    notafiscal = models.ForeignKey(NotaFiscal, on_delete=CASCADE)

    def __str__(self):
        return self.fornecedor
    
class ContasaReceber(models.Model):
    SITUACAO_BOLETO_CHOICES = [
        ('1', 'A vencer'),
        ('2', 'Vencido'),
        ('3', 'Protestado'),
        ('4', 'Pago até o vencimento'),
        ('5', 'Regularizado'),
    ]
    vencimento = models.DateField()
    valor = models.FloatField()
    cliente = models.ForeignKey(Cliente, on_delete=CASCADE)
    situacao = models.CharField( 
        max_length=25,
        choices=SITUACAO_BOLETO_CHOICES,
        default= '1')
    notafiscal = models.ForeignKey(NotaFiscal, on_delete=CASCADE)

    def __str__(self):
        return self.cliente