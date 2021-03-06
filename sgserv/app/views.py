from os import O_DIRECT, fpathconf
from django.db.models import fields
from django.forms import ModelForm
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import *

# Criando classe de formulário de clientes

class ClienteForm(ModelForm):
    class Meta: 
        model = Cliente
        fields = [ 
            'nome', 'natureza','cadastro_fiscal','telefone', 'email', 'endereco','data_cadastro','situacao',
        ]

# Criando classe de formulário de endereços

class EnderecoForm(ModelForm):
    class Meta:
        model = Endereco
        fields = [ 
            'logradouro','numero', 'bairro', 'cidade', 'uf', 'cep',
        ]

# Criando classe de formulário de fornecedores 

class FornecedorForm(ModelForm):
    class Meta:
        model = Fornecedor
        fields = [ 
            'nome', 'CNPJ', 'telefone', 'email', 'endereco',
        ]


# Criando classe de formulário de Equipamentos

class EquipamentosForm(ModelForm):
    class Meta:
        model = Equipamentos
        fields = [ 
            'nome', 'marca', 'modelo', 'serie', 'capacidade', 
        ]

# Criando classe de formulário de compromissos

class CompromissoForm(ModelForm):
    class Meta:
        model = Compromisso
        fields = [ 
            'id','data', 'hora', 'tipo', 'descricao', 'cliente', 'equipamentos', 'situacao',
        ]
        ordering = ['-data']

# Criando clase de formulário de notas fiscais

class NotaFiscalForm(ModelForm):
    class Meta:
        model = NotaFiscal
        fields = [ 
            'numero', 'tipo', 'fornecedor', 'valor',
        ]

# Criando classe de formulário de contas a pagar

class ContasaPagarForm(ModelForm):
    class Meta:
        model = ContasaPagar
        fields = [ 
            'vencimento', 'valor', 'fornecedor', 'situacao', 'notafiscal',
        ]

# Criando classe de formulário de contas a receber

class ContasReceberForm(ModelForm):
    class Meta:
        model = ContasaReceber
        fields = [
            'vencimento', 'valor', 'cliente', 'situacao', 'notafiscal',
        ]

# Rotina de cadastro de endereço protegida por login

@login_required
def cadastra_endereco(request, template_name='endereco/cadastra_endereco.html'):
    form_endereco = EnderecoForm(request.POST or None)
    if form_endereco.is_valid():
        form_endereco.save()
        return redirect('cadastro')
    return render(request, template_name, {'form_endereco': form_endereco})

# Rotina de cadastro de clientes protegida por login
@login_required
def cadastra_cliente(request, template_name='cliente/cadastra_cliente.html'):
    form_cliente = ClienteForm(request.POST or None)
    if form_cliente.is_valid():
        form_cliente.save()
        return redirect('dashboard')
    return render(request, template_name, {'form_cliente':form_cliente})

# Rotina de listagem de clientes protegida por login
@login_required
def lista_cliente(request, template_name='cliente/lista_cliente.html'):
    query = request.GET.get("busca")
    if query:
        cliente = Cliente.objects.filter(nome__icontains=query)
    else:
        cliente = Cliente.objects.all()
    clientes = {'cliente':cliente}
    return render(request, template_name, clientes)


# Rotina de cadastro de fornecedores protegida por login
@login_required
def cadastra_fornecedor(request, template_name='fornecedor/cadastra_fornecedor.html'):
    form_fornecedor = FornecedorForm(request.POST or None)
    if form_fornecedor.is_valid():
        form_fornecedor.save()
        return redirect('dashboard')
    return render(request, template_name, {'form_fornecedor': form_fornecedor})

# Rotina de cadastro de equipamentos protegida por login
@login_required
def cadastra_equipamento(request, template_name='equipamentos/cadastra_equipamento.html'):
    form_equipamento = EquipamentosForm(request.POST or None)
    if form_equipamento.is_valid():
        form_equipamento.save()
        return redirect('dashboard')
    return render(request, template_name, {'form_equipamento': form_equipamento})
# Rotina de cadastro de compromisso protegida por login
@login_required
def cadastra_compromisso(request, template_name='ordens/cadastra_compromisso.html'):
    form_compromisso = CompromissoForm(request.POST or None)
    if form_compromisso.is_valid():
        form_compromisso.save()
        return redirect('dashboard')
    return render(request, template_name, {'form_compromisso':form_compromisso})

# Rotina para listagem geral de ordens 
@login_required
def consulta_ordens(request, template_name='ordens/consulta_ordens.html'):
    ordens = Compromisso.objects.all().order_by('-data')
    return render(request, template_name, {'ordens':ordens})

# Rotina de construção de um dashboard protegida por login
@login_required
def dashboard(request, template_name='dashboard/dashboard.html'):
    compromisso = Compromisso.objects.all().order_by('data')
    contas_pagar = ContasaPagar.objects.all()
    contas_receber = ContasaReceber.objects.all().order_by('vencimento')
    fornecedor = Fornecedor.objects.all()
    return render(request, template_name, {'compromisso':compromisso, 'contas_pagar':contas_pagar, 'contas_receber':contas_receber, 'fornecedor':fornecedor})

# Rotina para detalhar ordem 
@login_required
def detalha_ordem(request, pk, template_name='ordens/detalha_ordem.html'):
    ordem = get_object_or_404(Compromisso, pk = pk)
    return render(request, template_name, {'ordem':ordem})

# Rotina para encerrar ordem
@login_required
def encerra_ordem(request, pk, template_name='ordens/encerra_ordem.html'):
    ordem = get_object_or_404(Compromisso, pk = pk)
    ordem.situacao = 2
    ordem.save()
    """ if request.method == 'POST':
        ordem_form = CompromissoForm(request.POST, instance= ordem)
        if ordem_form.is_valid():
            ordem_form.save()
            return redirect('dashboard')
    else:
       ordem_form = CompromissoForm(instance= ordem)"""
    return HttpResponseRedirect('/dashboard/dashboard')


# Rotina para efetuar login
def logar(request, template_name='login.html'):
    next = request.GET.get('next','/dashboard/dashboard')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(next)
        else:
            messages.error(request, 'Usuário ou senha inválidos!')
            return HttpResponseRedirect(settings.LOGIN_URL)
    
    return render(request, template_name,{'redirect_to':next})
# Rotina para efetuar logout
def deslogar(request):
    logout(request)
    return HttpResponseRedirect(settings.LOGIN_URL)


# Rotina para geração de página de controle da área financeira
@login_required
def painel_financeiro(request, template_name='financeiro/painel_financeiro.html'):
    return render(request, template_name)

# Rotina para cadastramento de notas fiscais
@login_required
def cadastra_nota_fiscal(request, template_name='fiscal/cadastra_nota_fiscal.html'):
    form_nota_fiscal = NotaFiscalForm(request.POST or None)
    if form_nota_fiscal.is_valid():
        form_nota_fiscal.save()
        return redirect('painel_financeiro')
    return render(request, template_name, {'form_nota_fiscal':form_nota_fiscal})


# Rotina para cadastramento de contas a pagar  
@login_required
def cadastra_contasapagar(request, template_name='contasapagar/cadastra_contasapagar.html'):
    form_contas_pagar = ContasaPagarForm(request.POST or None)
    if form_contas_pagar.is_valid():
        form_contas_pagar.save()
        return redirect('painel_financeiro')
    return render(request, template_name, {'form_contas_pagar': form_contas_pagar})

#Rotina para listagem de contas a pagar por fornecedor
@login_required
def lista_contas_pagar_fornecedor(request, pk, template_name='contasapagar/lista_fornecedor.html'):
    fornecedor = get_object_or_404(Fornecedor, pk = pk)
    contas_pagar = ContasaPagar.objects.filter(fornecedor = fornecedor.pk)
    return render(request, template_name, {'contas_pagar':contas_pagar, 'fornecedor':fornecedor})