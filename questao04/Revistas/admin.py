# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from Revistas.models import Colecao
from Revistas.models import CadastroDeRevista
from Revistas.models import CadastroDeAmigo
from Revistas.models import caixa
from Revistas.models import Emprestimo

admin.site.register(Colecao)
admin.site.register(CadastroDeRevista)
admin.site.register(CadastroDeAmigo)
admin.site.register(caixa)
admin.site.register(Emprestimo)
admin.site.site_header = 'Painel de Controle'