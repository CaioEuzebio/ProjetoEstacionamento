from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Pessoa, Veiculo, Mensalista, MovMensalista, MovRotativo

from .forms import PessoasForm, VeiculosForm, RotativosForm, MensalistaForm, MovMensalForm


def home(request):
    context = {'mensagem': 'Olá Mundo!'}
    return render(request, 'core/index.html', context)



def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    p_form = PessoasForm()
    p_data = {'pessoas': pessoas, 'p_form': p_form}
    return render(request, 'core/lista_pessoas.html', p_data)

def pessoa_novo(request):
    p_form = PessoasForm(request.POST or None)
    if  p_form.is_valid():
        p_form.save()
    return redirect('core_lista_pessoas')



def pessoa_update(request, id):   
    p_data = {}
    pessoa = Pessoa.objects.get(id=id)
    p_form = PessoasForm(request.POST or None, instance=pessoa)
    p_data['pessoa'] = pessoa
    p_data['p_form'] = p_form
    if request.method == 'POST':
        if p_form.is_valid():
            p_form.save()
            return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/update_pessoa.html', p_data)



def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    v_form = VeiculosForm()
    v_data = {'veiculos': veiculos, 'v_form': v_form}
    return render(request, 'core/lista_veiculos.html', v_data )


def veiculos_novo(request):
    v_form = VeiculosForm(request.POST or None)
    if  v_form.is_valid():
        v_form.save()
    return redirect('core_lista_veiculos')


def lista_rotativos(request):
    rotativos = MovRotativo.objects.all()
    r_form = RotativosForm()
    r_data = {'rotativos': rotativos, 'r_form': r_form}
    return render(request, 'core/lista_rotativos.html', r_data)

def rotativos_novo(request):
    r_form = RotativosForm(request.POST or None)
    if  r_form.is_valid():
        r_form.save()
    return redirect('core_lista_rotativos')


def lista_mensalistas(request):
    mensalistas = Mensalista.objects.all()
    m_form = MensalistaForm()
    m_data = {'mensalistas': mensalistas, 'm_form': m_form}
    return render(request, 'core/lista_mensalistas.html', m_data)


def mensalista_novo(request):
    m_form = MensalistaForm(request.POST or None)
    if  m_form.is_valid():
        m_form.save()
    return redirect('core_lista_mensalistas')


def lista_mov_mensalistas(request):
    movmensalistas = MovMensalista.objects.all()
    mm_form = MovMensalForm()
    mm_data = {'movmensalistas': movmensalistas, 'mm_form': mm_form}
    return render(request, 'core/lista_mov_mensalistas.html', mm_data)

def mov_mensalistas_novo(request):
    mm_form = MovMensalForm(request.POST or None)
    if  mm_form.is_valid():
        mm_form.save()
    return redirect('core_lista_mov_mensalistas')

