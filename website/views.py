from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contato
from django.urls import path



def website_home(request):
    return render(request, 'website/index.html')



def servicos(request):
    return render(request, 'website/servicos.html')



def sobre(request):
    return render(request, 'website/sobre.html')



def planos(request):
    return render(request, 'website/planos.html')


def contato(request):
    erro = ''
    if request.method == 'POST':
        try:
            contato = {}
            contato['email'] = request.POST.get('email')
            contato['nome'] = request.POST.get('nome')
            contato['sobrenome'] = request.POST.get('sobrenome')
            contato['estado'] = request.POST.get('estado')
            contato['mensagem'] = request.POST.get('mensagem')
            contato['receber_promocoes'] = True if request.POST.get('receber_promocoes') == 'on' else False

            Contato.objects.create(**contato)
            
        except Exception as e:
            erro = str(e)
        else:
            erro = 'Mensagem enviada com sucesso!'

    return render(request, 'website/contato.html', {'erro':erro})



