# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from core.models import Despesa

class DespesaAdmin(admin.ModelAdmin):
    list_display = ('data_criacao', 'tipo_despesa', 'descricao', 'forma_pagamento', 'vencimento', 'quitado',)

    date_hierarchy = 'vencimento'
    list_filter = ('quitado',)


admin.site.register(Despesa,DespesaAdmin)