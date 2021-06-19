from collections import namedtuple
from django.urls.conf import path
from . import views

urlpatterns= [ 
    path('login', views.logar, name='login'),
    path('/deslogar/', views.deslogar, name='deslogar'),
    path('cliente/cadastra_cliente', views.cadastra_cliente, name='cadastra_cliente'),
    path('cliente/lista_cliente', views.lista_cliente, name='lista_cliente'),
    path('endereco/cadastra_endereco', views.cadastra_endereco, name='cadastra_endereco'),
    path('fornecedor/cadastra_fornecedor', views.cadastra_fornecedor, name='cadastra_fornecedor'),
    path('compromisso/cadastra_compromisso', views.cadastra_compromisso, name= 'cadastra_compromisso'),
    path('dashboard/dashboard', views.dashboard, name='dashboard'),
] 