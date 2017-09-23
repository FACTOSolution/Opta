from django.shortcuts import render
from .projeto_view import get_total_vagas, filtrar_projetos

def mostrar(request):
    total_vagas = get_total_vagas()
    data = {}
    data['total_vagas'] = total_vagas
    return render(request, 'index.html', data)

def buscar_oportunidade(request):
    curso = request.GET['curso']
    palavra_chave = request.GET['palavra_chave']
    projetos = filtrar_projetos(curso, palavra_chave)
    data = {}
    data['projetos'] = projetos
    return render(request, 'opta_app/resultado_busca.html', data)
