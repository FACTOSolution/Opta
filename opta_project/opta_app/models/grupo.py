from django.db import models

# titulo
# descricao
# link site
# area
# centro
# curso/departamento

# Relacionamento Grupo-Professor (n - n)
# Relacionamento Grupo-Projeto (1 - n)

class Grupo(models.Model):
    nome = models.CharField(max_length=80)
    descricao = models.TextField(default='Sem descrição')
    site = models.URLField(max_length=80, blank=True)
    area = models.CharField(max_length=40, blank=True)
    centro = models.CharField(max_length=50, blank=True)
    curso = models.CharField(max_length=40, blank=True)
