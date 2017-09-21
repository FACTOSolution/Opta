from django import forms
from .models import Professor, Grupo, Projeto
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['area', 'subarea', 'lattes']

class GrupoForm(forms.ModelForm):
    class Meta:
        model = Grupo
        fields = ['nome', 'descricao', 'site', 'area', 'centro', 'curso']

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['titulo', 'subtitulo', 'descricao', 'requisitos', 'vagas']
