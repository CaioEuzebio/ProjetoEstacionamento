from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Pessoa, Veiculo, Mensalista, MovMensalista

from .forms import PessoasForm


def home(request):
    context = {'mensagem': 'Olá Mundo!'}
    return render(request, 'core/index.html', context)



def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    form = PessoasForm()
    data = {'pessoas': pessoas, 'form': form}
    return render(request, 'core/lista_pessoas.html', data)

def pessoa_novo(request):
    form = PessoasForm(request.POST or None)
    if  form.is_valid():
        form.save()
    return redirect('core_lista_pessoas')


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

