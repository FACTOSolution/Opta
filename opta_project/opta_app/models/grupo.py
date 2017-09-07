from django.db import models
from django.contrib.auth.models import User

class Grupo(models.Model):
    # Fields
    nome = models.CharField(max_length=80)
    descricao = models.TextField(default='Sem descrição')
    site = models.URLField(max_length=80, blank=True)
    area = models.CharField(max_length=40, blank=True)
    centro = models.CharField(max_length=50, blank=True)
    curso = models.CharField(max_length=40, blank=True)

    # Relationship field
    professores = models.ManyToManyField(User, through='ProfessorGrupo')
