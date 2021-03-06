# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-02 16:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40, verbose_name='Nome')),
                ('Carga_Horaria', models.IntegerField()),
                ('ementa', models.CharField(max_length=40, verbose_name='Ementa')),
                ('Valor', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40, verbose_name='Nome')),
                ('telefone', models.CharField(max_length=15, verbose_name='Telefone')),
                ('Valor_Hora_Aula', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
            ],
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Data_inicio', models.DateField(verbose_name='Data inicio')),
                ('Data_termino', models.DateField(verbose_name='Data termino')),
                ('Hora_inicio', models.TimeField()),
                ('Hora_termino', models.TimeField()),
                ('Professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursos.Professor')),
            ],
        ),
    ]
