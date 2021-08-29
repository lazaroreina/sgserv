from collections import namedtuple
from os import pardir
from django.urls.conf import path
from . import views

urlpatterns= [ 
    path('login', views.logar, name='login'),
    path('/deslogar/', views.deslogar, name='deslogar'),
    path('cliente/cadastra_cliente', views.cadastra_cliente, name='cadastra_cliente'),
    path('cliente/lista_cliente', views.lista_cliente, name='lista_cliente'),
    path('equipamentos/cadastra_equipamento', views.cadastra_equipamento, name='cadastra_equipamento'),
    path('endereco/cadastra_endereco', views.cadastra_endereco, name='cadastra_endereco'),
    path('fornecedor/cadastra_fornecedor', views.cadastra_fornecedor, name='cadastra_fornecedor'),
    path('compromisso/cadastra_compromisso', views.cadastra_compromisso, name= 'cadastra_compromisso'),
    path('ordens/detalha_ordem/<int:pk>/', views.detalha_ordem, name='detalha_ordem'),
    path('dashboard/dashboard', views.dashboard, name='dashboard'),
    path('financeiro/painel_financeiro', views.painel_financeiro, name= 'painel_financeiro'),
    path('contasapagar/cadastra_contasapagar', views.cadastra_contasapagar, name= 'cadastra_contasapagar'),
    path('fiscal/cadastra_nota_fiscal', views.cadastra_nota_fiscal, name= 'cadastra_nota_fiscal'),
    path('contasapagar/lista_contas_pagar_fornecedor/<int:pk>/', views.lista_contas_pagar_fornecedor, name= 'lista_contas_pagar_fornecedor'),

] 