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
                    pessoa_update,
                    veiculo_update,
                    update_rotativos,
                    update_mensalistas,
                    update_mov_mensalistas,
                    pessoa_delete,
                    veiculo_delete,
                    rotativos_delete,
                    mensalista_delete,
                    movmensalistas_delete )



urlpatterns = [
    url(r'^$', home, name='core_home'),
    url(r'^pessoas/$', lista_pessoas, name='core_lista_pessoas'),
    url(r'^pessoa-novo/$', pessoa_novo, name='core_pessoa_novo'),
    url(r'^pessoa-update/(?P<id>\d+)/$', pessoa_update, name='core_pessoa_update'),
    url(r'^pessoa-delete/(?P<id>\d+)/$', pessoa_delete, name='core_pessoa_delete'),

    url(r'^veiculos-novo/$', veiculos_novo, name='core_veiculos_novo'),
    url(r'^veiculo/$', lista_veiculos, name='core_lista_veiculos'),
    url(r'^veiculo-update/(?P<id>\d+)/$', veiculo_update, name='core_veiculo_update'),
    url(r'^veiculo-delete/(?P<id>\d+)/$', veiculo_delete, name='core_veiculo_delete'),


    url(r'^rotativos/$', lista_rotativos, name='core_lista_rotativos'),
    url(r'^rotativos-novo/$', rotativos_novo, name='core_rotativos_novo'),
    url(r'^update-rotativos/(?P<id>\d+)/$', update_rotativos, name='core_update_rotativos'),
    url(r'^rotativos-delete/(?P<id>\d+)/$', rotativos_delete, name='core_delete_rotativos'),

    url(r'^mensalistas/$', lista_mensalistas, name='core_lista_mensalistas'),
    url(r'^mensalista-novo/$', mensalista_novo, name='core_mensalista_novo'),
    url(r'^update-mensalistas/(?P<id>\d+)/$', update_mensalistas, name='core_update_mensalistas'),
    url(r'^mensalistas-delete/(?P<id>\d+)/$', mensalista_delete, name='core_delete_mensalistas'),


    url(r'^mov-mensalistas/$', lista_mov_mensalistas, name='core_lista_mov_mensalistas'),
    url(r'^mov-mensalistas-novo/$', mov_mensalistas_novo, name='core_mov_mensalistas_novo'),
    url(r'^update-mov-mensalistas/(?P<id>\d+)/$', update_mov_mensalistas, name='core_update_mov_mensalistas'),
    url(r'^mov-mensalistas-delete/(?P<id>\d+)/$', movmensalistas_delete, name='core_delete_mov_mensalistas')




]
