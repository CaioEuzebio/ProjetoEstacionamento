
from django.conf.urls import url, include
from .views import website_home, contato, servicos, sobre, planos
from django.urls import path
from django.contrib import admin




urlpatterns = [
    
    url(r'^$', website_home, name='website_home'),
    url(r'^sistema/', include('core.urls')),
    url(r'^contato$', contato, name='contato'),
    url(r'^servicos$', servicos, name='servicos'),
    url(r'^sobre$', sobre, name='sobre'),
    url(r'^planos$', planos, name='planos'),
]
