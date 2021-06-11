from django.db.models import fields
from django.forms import ModelForm
from django.shortcuts import redirect, render
from .models import *
# Create your views here.

class ClienteForm(ModelForm):
    class Meta: 
        model = Cliente
        fields = [ 
            'nome', 'telefone', 'email', 'endereco',
        ]

class EnderecoForm(ModelForm):
    class Meta:
        model = Endereco
        fields = [ 
            'logradouro','numero', 'bairro', 'cidade', 'uf', 'cep',
        ]

class FornecedorForm(ModelForm):
    class Meta:
        model = Fornecedor
        fields = [ 
            'nome', 'CNPJ', 'telefone', 'email', 'endereco',
        ]

class CompromissoForm(ModelForm):
    class Meta:
        model = Compromisso
        fields = [ 
            'data', 'hora', 'descricao', 'cliente',
        ]

def cadastra_endereco(request, template_name='endereco/cadastra_endereco.html'):
    form_endereco = EnderecoForm(request.POST or None)
    if form_endereco.is_valid():
        form_endereco.save()
        return redirect('index')
    return render(request, template_name, {'form_endereco': form_endereco})


def cadastra_cliente(request, template_name='cliente/cadastra_cliente.html'):
    form_cliente = ClienteForm(request.POST or None)
    if form_cliente.is_valid():
        form_cliente.save()
        return redirect('index')
    return render(request, template_name, {'form_cliente':form_cliente})

def cadastra_fornecedor(request, template_name='fornecedor/cadastra_fornecedor.html'):
    form_fornecedor = FornecedorForm(request.POST or None)
    if form_fornecedor.is_valid():
        form_fornecedor.save()
        return redirect('index')
    return render(request, template_name, {'form_fornecedor': form_fornecedor})

def cadastra_compromisso(request, template_name='compromisso/cadastra_compromisso.html'):
    form_compromisso = CompromissoForm(request.POST or None)
    if form_compromisso.is_valid():
        form_compromisso.save()
        return redirect('index')
    return render(request, template_name, {'form_compromisso':form_compromisso})

def pagina(request, template_name='index.html'):
    texto = 'funcionow'
    return render(request, template_name, {'texto':texto})