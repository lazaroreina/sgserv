from django.urls.conf import path
from . import views

urlpatterns= [ 
    path('index', views.pagina, name='index'),
    path('cliente/cadastra_cliente', views.cadastra_cliente, name='cadastra_cliente'),
    path('endereco/cadastra_endereco', views.cadastra_endereco, name='cadastra_endereco'),
    path('fornecedor/cadastra_fornecedor', views.cadastra_fornecedor, name='cadastra_fornecedor'),
    path('compromisso/cadastra_compromisso', views.cadastra_compromisso, name= 'cadastra_compromisso')

]