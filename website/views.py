from django.shortcuts import render

def website_home(request):
    return render(request, 'website/index.html')

def contato(request):
    return render(request, 'website/contato.html')


