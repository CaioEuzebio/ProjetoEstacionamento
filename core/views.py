from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Pessoa, Veiculo, Mensalista, MovMensalista

from .forms import PessoasForm


def home(request):
    context = {'mensagem': 'Olá Mundo!'}
    return render(request, 'core/index.html', context)



def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    p_form = PessoasForm()
    p_data = {'pessoas': pessoas, 'p_form': p_form}
    return render(request, 'core/lista_pessoas.html', data)

def pessoa_novo(request):
    p_form = PessoasForm(request.POST or None)
    if  p_form.is_valid():
        p_form.save()
    return redirect('core_lista_pessoas')


def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    v_data = {'veiculos': veiculos}
    return render(request, 'core/lista_veiculos.html', v_data )




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

