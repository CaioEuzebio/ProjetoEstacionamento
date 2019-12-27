from django.conf.urls import url, include
from .views import ( home, 
                    lista_pessoas, 
                    lista_veiculos, 
                    lista_rotativos )

urlpatterns = [
    url(r'^$', home, name='core_home'),
    url(r'^pessoas/$', lista_pessoas, name='core_lista_pessoas'),
    url(r'^veiculo/$', lista_veiculos, name='core_lista_veiculos'),
    url(r'^mov-rot-list/$', lista_rotativos, name='core_lista_rotativos')

]
