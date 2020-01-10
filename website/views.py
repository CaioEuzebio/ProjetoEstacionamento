from django.shortcuts import render
from .models import Contato

def website_home(request):
    return render(request, 'website/index.html')

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


