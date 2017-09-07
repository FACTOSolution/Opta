from django.db import models
from django.contrib.auth.models import User
from .grupo import Grupo

# Intermediary model
class ProfessorGrupo(models.Model):
    professor = models.ForeignKey(User)
    grupo = models.ForeignKey(Grupo)
