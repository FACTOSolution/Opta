from django.db import models

# nome
# email
# area
# subarea
# curriculo

# Relacionamento Professor-Grupo (n - n)
# Relacionamento Professor-Projeto (1 - n)

class Professor(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=40, default='')
    area = models.CharField(max_length=40, blank=True)
    subarea = models.CharField(max_length=40, blank=True)
    lattes = models.URLField(max_length=80, blank=True)
