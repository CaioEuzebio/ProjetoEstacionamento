from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Pessoa, Veiculo, Mensalista, MovMensalista, MovRotativo
from .forms import PessoasForm, VeiculosForm, RotativosForm, MensalistaForm, MovMensalForm
from django.contrib.auth.decorators import login_required



# Home Page

@login_required
def home(request):
    context = {'mensagem': 'Essa é a pagina inicial!'}
    return render(request, 'core/index.html', context)


# Pessoas Functions

@login_required
def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    p_form = PessoasForm()
    p_data = {'pessoas': pessoas, 'p_form': p_form}
    return render(request, 'core/lista_pessoas.html', p_data)

@login_required
def pessoa_novo(request):
    p_form = PessoasForm(request.POST or None)
    if  p_form.is_valid():
        p_form.save()
    return redirect('core_lista_pessoas')


@login_required
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


@login_required
def pessoa_delete(request, id):   
    pessoa = Pessoa.objects.get(id=id)
    if request.method == 'POST':
            pessoa.delete()
            return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/delete_pessoa_confirm.html', {'pessoa': pessoa})


# Veiculos Functions

@login_required
def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    v_form = VeiculosForm()
    v_data = {'veiculos': veiculos, 'v_form': v_form}
    return render(request, 'core/lista_veiculos.html', v_data )

@login_required
def veiculos_novo(request):
    v_form = VeiculosForm(request.POST or None)
    if  v_form.is_valid():
        v_form.save()
    return redirect('core_lista_veiculos')

@login_required
def veiculo_update(request, id):   
    v_data = {}
    veiculo = Veiculo.objects.get(id=id)
    v_form = VeiculosForm(request.POST or None, instance=veiculo)
    v_data['veiculo'] = veiculo
    v_data['v_form'] = v_form
    if request.method == 'POST':
        if v_form.is_valid():
            v_form.save()
            return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/veiculo_update.html', v_data)    


@login_required    
def veiculo_delete(request, id):   
    veiculo = Veiculo.objects.get(id=id)
    if request.method == 'POST':
            veiculo.delete()
            return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/delete_veiculo_confirm.html', {'veiculo': veiculo})


# Rotativos Functions

@login_required
def lista_rotativos(request):
    rotativos = MovRotativo.objects.all()
    r_form = RotativosForm()
    r_data = {'rotativos': rotativos, 'r_form': r_form}
    return render(request, 'core/lista_rotativos.html', r_data)
@login_required
def rotativos_novo(request):
    r_form = RotativosForm(request.POST or None)
    if  r_form.is_valid():
        r_form.save()
    return redirect('core_lista_rotativos')

@login_required
def update_rotativos(request, id):   
    r_data = {}
    rotativos = MovRotativo.objects.get(id=id)
    r_form = RotativosForm(request.POST or None, instance=rotativos)
    r_data['rotativos'] = rotativos
    r_data['r_form'] = r_form
    if request.method == 'POST':
        if r_form.is_valid():
            r_form.save()
            return redirect('core_lista_rotativos')
    else:
        return render(request, 'core/update_rotativos.html', r_data)

@login_required
def rotativos_delete(request, id):   
    rotativos = MovRotativo.objects.get(id=id)
    if request.method == 'POST':
            rotativos.delete()
            return redirect('core_lista_rotativos')
    else:
        return render(request, 'core/delete_rotativos_confirm.html', {'rotativos': rotativos})


# Mensalistas Functions

@login_required
def lista_mensalistas(request):
    mensalistas = Mensalista.objects.all()
    m_form = MensalistaForm()
    m_data = {'mensalistas': mensalistas, 'm_form': m_form}
    return render(request, 'core/lista_mensalistas.html', m_data)

@login_required
def mensalista_novo(request):
    m_form = MensalistaForm(request.POST or None)
    if  m_form.is_valid():
        m_form.save()
    return redirect('core_lista_mensalistas')

@login_required
def update_mensalistas(request, id):   
    m_data = {}
    mensalistas = Mensalista.objects.get(id=id)
    m_form = MensalistaForm(request.POST or None, instance=mensalistas)
    m_data['mensalistas'] = mensalistas
    m_data['m_form'] = m_form
    if request.method == 'POST':
        if m_form.is_valid():
            m_form.save()
            return redirect('core_lista_mensalistas')
    else:
        return render(request, 'core/update_mensalistas.html', m_data) 

@login_required
def mensalista_delete(request, id):   
    mensalistas = Mensalista.objects.get(id=id)
    if request.method == 'POST':
            mensalistas.delete()
            return redirect('core_lista_mensalistas')
    else:
        return render(request, 'core/delete_mensalistas_confirm.html', {'mensalistas': mensalistas})


# MovMensalistas Functions

@login_required
def lista_mov_mensalistas(request):
    mm_data = {}
    movmensalistas = MovMensalista.objects.all()
    mm_form = MovMensalForm()
    mm_data = {'movmensalistas': movmensalistas, 'mm_form': mm_form}
    return render(request, 'core/lista_mov_mensalistas.html', mm_data)


@login_required
def mov_mensalistas_novo(request):
    mm_form = MovMensalForm(request.POST or None)
    if  mm_form.is_valid():
        mm_form.save()
    return redirect('core_lista_mov_mensalistas')

@login_required    
def update_mov_mensalistas(request, id):   
    mm_data = {}
    movmensalistas = MovMensalista.objects.get(id=id)
    mm_form = MovMensalForm(request.POST or None, instance=movmensalistas)
    mm_data['movmensalistas'] = movmensalistas
    mm_data['mm_form'] = mm_form
    if request.method == 'POST':
        if mm_form.is_valid():
            mm_form.save()
            return redirect('core_lista_mov_mensalistas')
    else:
        return render(request, 'core/update_mov_mensalistas.html', mm_data) 

@login_required
def movmensalistas_delete(request, id):   
    movmensalistas = MovMensalista.objects.get(id=id)
    if request.method == 'POST':
            movmensalistas.delete()
            return redirect('core_lista_mov_mensalistas')
    else:
        return render(request, 'core/delete_mov_mensalistas.html', {'movmensalistas': movmensalistas})


