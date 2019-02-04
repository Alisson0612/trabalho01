# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from cursos.models import Curso
from cursos.models import Turma
from cursos.models import Professor

class TurmaInline(admin.TabularInline):
    model = Turma

class ProfessorAdmin(admin.ModelAdmin):
    inlines = [
        TurmaInline,
    ]


admin.site.register(Curso)
admin.site.register(Turma)
admin.site.register(Professor)