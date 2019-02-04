# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Curso(models.Model):
    nome = models.CharField('Nome',max_length=40)
    Carga_Horaria = models.IntegerField()
    ementa = models.CharField('Ementa', max_length=40)
    Valor = models.FloatField()
    class Meta:
        verbose_name_plural = 'Cursos'
    def __str__(self):
        return self.nome

class Professor(models.Model):

    nome = models.CharField('Nome',max_length=40)
    telefone = models.CharField('Telefone',max_length=15)
    Valor_Hora_Aula = models.DecimalField(max_digits=20,decimal_places=2,default=0)
    def __str__(self):
        return self.nome

class Turma(models.Model):
    Professor = models.ForeignKey(Professor,on_delete=models.CASCADE)
    Data_inicio = models.DateField('Data inicio')
    Data_termino = models.DateField('Data termino')
    Hora_inicio = models.TimeField()
    Hora_termino = models.TimeField()
    def __str__(self):
        return self.Data_inicio
class Meta:
    verbose_name_plural = 'Controles Academioos'
    verbose_name = 'Controle Academico'

