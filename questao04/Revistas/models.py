# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


GrupoAmigo_choices = (
    ('',(
        ('predio','Predio'),
        ('escola','Escola'),
    ),

    ),
)

class Colecao(models.Model):
    nome = models.CharField('Nome ', max_length=30)

    def __str__(self):
        return self.nome
    

class CadastroDeRevista(models.Model):
    numero_edicao = models.IntegerField()
    ano = models.IntegerField()
    def __str__(self):
        return self.numero_edicao
    

class CadastroDeAmigo(models.Model):
    nome = models.CharField('Nome',max_length=20)
    nome_mae = models.CharField('Nome da Mãe',max_length=20)
    telefone = models.CharField('Telefone',max_length=15)
    grupo_amigo = models.CharField('Grupo de Amigos',max_length=20, choices=GrupoAmigo_choices, default='')
    
    def __str__(self):
        return self.nome
    
class caixa(models.Model):
    Numero = models.IntegerField()
    etiqueta = models.CharField('Etiqueta',max_length=20)
    cor = models.CharField('Cor',max_length=10)

    def __str__(self):
        return self.etiqueta
    

class Emprestimo(models.Model):
    data_emprestimo = models.DateField('Data do Emprestimo')
    data_devolucao = models.DateField('Data da Devoluçao')
    def __str__(self):
        return self.data_emprestimo
    
