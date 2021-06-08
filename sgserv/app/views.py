from django.db.models import fields
from django.forms import ModelForm
from django.shortcuts import render
from .models import *
# Create your views here.

class ClienteForm(ModelForm):
    class Meta: 
        model = Cliente
        fields = [ 
            'nome', 'telefone', 'email', 'endereco',
        ]

def lista(request, template_name='lista.html'):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, template_name, {'form':form})
