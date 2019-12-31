from django.conf.urls import url, include
from .views import ( home, 
                    lista_pessoas, 
                    lista_veiculos, 
                    lista_rotativos,
                    lista_mensalistas,
                    lista_mov_mensalistas,
                    pessoa_novo,
                    veiculos_novo,
                    rotativos_novo,
                    mensalista_novo,
                    mov_mensalistas_novo,
                    pessoa_update )


urlpatterns = [
    url(r'^$', home, name='core_home'),
    url(r'^pessoas/$', lista_pessoas, name='core_lista_pessoas'),
    url(r'^pessoa-novo/$', pessoa_novo, name='core_pessoa_novo'),
    url(r'^pessoa-update/(?P<id>\d+)/$', pessoa_update, name='core_pessoa_update'),

    url(r'^veiculos-novo/$', veiculos_novo, name='core_veiculos_novo'),
    url(r'^veiculo/$', lista_veiculos, name='core_lista_veiculos'),

    url(r'^rotativos/$', lista_rotativos, name='core_lista_rotativos'),
    url(r'^rotativos-novo/$', rotativos_novo, name='core_rotativos_novo'),

    url(r'^mensalistas/$', lista_mensalistas, name='core_lista_mensalistas'),
    url(r'^mensalista-novo/$', mensalista_novo, name='core_mensalista_novo'),

    url(r'^mov-mensalistas/$', lista_mov_mensalistas, name='core_lista_mov_mensalistas'),
    url(r'^mov-mensalistas-novo/$', mov_mensalistas_novo, name='core_mov_mensalistas_novo')



]
