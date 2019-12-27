from django.shortcuts import render
from django.http import HttpResponse
from .models import Pessoa, Veiculo, Mensalista, MovMensalista

from .forms import PessoaForm


def home(request):
    context = {'mensagem': 'Olá Mundo!'}
    return render(request, 'core/index.html', context)



def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    return render(request, 'core/lista_pessoas.html', 
                            {'pessoas': pessoas})


def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    return render(request, 'core/lista_veiculos.html', 
                            {'veiculos': veiculos})


def lista_rotativos(request):
    rotativo = MovRotativo.objects.all()
    return render(request, 'core/lista_rotativos.html', 
                            {'rotativos': rotativos})


def lista_mensalistas(request):
    mensalistas = Mensalista.objects.all()
    return render(request, 'core/lista_mensalistas.html', 
                            {'mensalistas': mensalistas})


def lista_mov_mensalistas(request):
    movmensalistas = MovMensalista.objects.all()
    return render(request, 'core/lista_mov_mensalistas.html', 
                            {'movmensalistas': movmensalistas})

