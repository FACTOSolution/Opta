from django.contrib import admin
from .models import Professor, Grupo, Projeto, ProfessorGrupo

# Enables crud actions from django admin site
admin.site.register(Professor)
admin.site.register(Grupo)
admin.site.register(Projeto)
admin.site.register(ProfessorGrupo)
