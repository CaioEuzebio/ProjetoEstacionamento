from django.conf.urls import url, include
from .views import ( home, 
                    lista_pessoas, 
                    lista_veiculos, 
                    lista_rotativos,
                    lista_mensalistas,
                    lista_mov_mensalistas )

urlpatterns = [
    url(r'^$', home, name='core_home'),
    url(r'^pessoas/$', lista_pessoas, name='core_lista_pessoas'),
    url(r'^veiculo/$', lista_veiculos, name='core_lista_veiculos'),
    url(r'^rotativos/$', lista_rotativos, name='core_lista_rotativos'),
    url(r'^mensalistas/$', lista_mensalistas, name='core_lista_mensalistas'),
    url(r'^mov-mensalistas/$', lista_mov_mensalistas, name='core_lista_mov_mensalistas')

]
