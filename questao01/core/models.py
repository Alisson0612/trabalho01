# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

TipoDespesa_choices = (
    ('', (
        ('remedio', 'Remédio'),
        ('roupas', 'Roupas'),
        ('alimentos', 'Alimentação'),
        ('educacao', 'Educação'),
        ('transporte', 'Transporte'),
        ('outros', 'Outros'),
    ),

     ),
)

FormaPagamento_choices = (
    ('', (
        ('dinheiro', 'Dinheiro'),
        ('cartao credito', 'Cartão de Crédito'),
        ('cartao debito', 'Cartão de Débito'),
        ('cartao crediario', 'Cartão Crediário'),
        ('cheque', 'Cheque'),
        ),
     ),
)

class Despesa(models.Model):
    data_criacao = models.CharField('Data de Criação',max_length=15)
    tipo_despesa = models.CharField('Tipo de Despesa', max_length=150, choices=TipoDespesa_choices, default='')
    descricao = models.TextField('Descrição')
    forma_pagamento = models.CharField('Forma de Pagamento', max_length=40, choices=FormaPagamento_choices, default='')
    vencimento = models.DateField('Vencimento')
    quitado = models.BooleanField('Quitado')

    class Meta:
        verbose_name_plural = 'Despesas'
        verbose_name = 'Despesa'