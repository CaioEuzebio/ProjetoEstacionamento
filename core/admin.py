from django.contrib import admin
from .models import (Pessoa, 
                    Veiculo, 
                    Marca, 
                    Parametros, 
                    MovRotativo,
                    Mensalista,
                    MovMensalista)



class MovRotativoAdmin(admin.ModelAdmin):
    list_display = [('veiculo'),('checkin'), ('checkout'), ('valor_hora'), ('horas_total') , ('pago'), ('total')]

    def veiculo(self, obj):
        return obj.veiculo


class MovMensalistaAdmin(admin.ModelAdmin):
    list_display = [('inicio'),('datapagamento'), ('total')]

    def inicio(self, obj):
        return obj.mensalista





admin.site.register(Marca)
admin.site.register(Veiculo)
admin.site.register(Pessoa)
admin.site.register(Parametros)
admin.site.register(MovRotativo, MovRotativoAdmin)
admin.site.register(Mensalista)
admin.site.register(MovMensalista, MovMensalistaAdmin)


