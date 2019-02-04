# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
# -*- coding: utf-8 -*-


from Temas.models import Tema
from Temas.models import ItemTema
from Temas.models import Aluguel
from Temas.models import Endereco
from Temas.models import Cliente


class TemaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'valorAluguel', 'corToalha')
    search_fields = ('nome',)

class ItemTemaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')
    search_fields = ('nome',)

class AluguelAdmin(admin.ModelAdmin):
    list_display = ('dataFesta', 'horaInicio', 'horaTermino', 'valorCobrado')
    list_filter = ('dataFesta',)

class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('logradouro', 'numero', 'complemento', 'bairro', 'cidade', 'uf', 'cep')
    search_fields = ('logradouro', )

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone')
    search_fields = ('nome',)
    list_filter = ('nome',)
admin.site.register(Tema, TemaAdmin)
admin.site.register(ItemTema, ItemTemaAdmin)
admin.site.register(Aluguel, AluguelAdmin)
admin.site.register(Endereco, EnderecoAdmin)
admin.site.register(Cliente, ClienteAdmin)


admin.site.site_header = 'Painel de Controle'
admin.site.index_title = 'Recursos'
admin.site.site_title = 'Título do Site'

