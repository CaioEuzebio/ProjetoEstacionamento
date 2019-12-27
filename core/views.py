from django.shortcuts import render
from django.http import HttpResponse
from .models import Pessoa, Veiculo, MovRotativo




def home(request):
    context = {'mensagem': 'Olá Mundo!'}
    return render(request, 'core/index.html', context)



def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'core/lista_pessoas.html', {'pessoas': pessoas})


def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    return render(request, 'core/lista_veiculos.html', {'veiculos': veiculos})


def lista_rotativos(request):
    rotativos = MovRotativo.objects.all()
    return render(request, 'core/lista_rotativos.html', {'rotativos': rotativos})
