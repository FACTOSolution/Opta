from django import forms
from .models import Professor
from django.core.exceptions import ValidationError

class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['area', 'subarea', 'lattes']
