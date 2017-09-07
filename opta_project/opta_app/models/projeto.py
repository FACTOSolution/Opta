from django.db import models
from django.contrib.auth.models import User
from .grupo import Grupo

class Projeto(models.Model):
    # Fields
    titulo = models.CharField(max_length=255)
    subtitulo = models.CharField(max_length=150, blank=True)
    descricao = models.TextField(default='Sem descrição')
    requisitos = models.TextField(default='Sem requisitos')
    vagas = models.PositiveSmallIntegerField(default=0)
    
    # Relationships fields
    professor = models.ForeignKey(User, on_delete=models.CASCADE)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
