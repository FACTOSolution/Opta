from django.shortcuts import render
from .projeto_view import get_total_vagas

def mostrar(request):
    total_vagas = get_total_vagas()
    data = {}
    data['total_vagas'] = total_vagas
    return render(request, 'index.html', data)
