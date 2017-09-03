from django.db import models

# titulo
# subtitulo
# descricao
# requisitos
# vagas

# Relacionamento Projeto-Professor (n - 1)
# Relacionamento Projeto-Grupo (n - 1)

class Projeto(models.Model):
    titulo = models.CharField(max_length=255)
    subtitulo = models.CharField(max_length=150, blank=True)
    descricao = models.TextField(default='Sem descrição')
    requisitos = models.TextField(default='Sem requisitos')
    vagas = models.PositiveSmallIntegerField(default=0)
