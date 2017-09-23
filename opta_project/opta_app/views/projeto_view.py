from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from ..models import Projeto, Professor, Grupo
from ..forms import ProjetoForm

def ver_projeto(request, pk_proj,  template_name='opta_app/detalhe_projeto.html'):
    projeto = get_object_or_404(Projeto, pk=pk_proj)
    data = {}
    data['projeto'] = projeto
    return render(request, template_name, data)

@login_required
def mostrar_projeto(request, pk_prof, pk_grupo, pk_proj,  template_name='opta_app/detalhe_projeto.html'):
    professor = get_object_or_404(Professor, pk=pk_prof)
    if request.user.professor == professor:
        projeto = get_object_or_404(Projeto, pk=pk_proj)
        data = {}
        data['projeto'] = projeto
        return render(request, template_name, data)
    return redirect('mostrar_professor')

@login_required
def listar_projeto(request, template_name='opta_app/lista_projeto.html'):
    projetos = Projeto.objects.all()
    data = {}
    data['object_list'] = projetos
    return render(request, template_name, data)

@login_required
def criar_projeto(request, pk_prof, pk_grupo, template_name='opta_app/form_projeto.html'):
    professor = get_object_or_404(Professor, pk=pk_prof)
    if request.user.professor == professor:
        grupo = get_object_or_404(Grupo, pk=pk_grupo)
        form = ProjetoForm(request.POST or None)
        if form.is_valid():
            proj_obj = form.cleaned_data
            titulo = proj_obj['titulo']
            subtitulo = proj_obj['subtitulo']
            descricao = proj_obj['descricao']
            requisitos = proj_obj['requisitos']
            vagas = proj_obj['vagas']
            projeto = Projeto.objects.create(
                titulo=titulo, subtitulo=subtitulo, descricao=descricao,
                requisitos=requisitos, vagas=vagas, professor=request.user, grupo=grupo)
            return redirect('mostrar_grupo', pk_prof, pk_grupo)
        return render(request, template_name, {'form':form})
    return redirect('mostrar_professor')

@login_required
def atualizar_projeto(request, pk_prof, pk_grupo, pk_proj, template_name='opta_app/form_projeto.html'):
    professor = get_object_or_404(Professor, pk=pk_prof)
    if request.user.professor == professor:
        projeto = get_object_or_404(Projeto, pk=pk_proj)
        form = ProjetoForm(request.POST or None, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect('mostrar_grupo', pk_prof, pk_grupo)
        return render(request, template_name, {'form':form})
    return redirect('mostrar_professor')

@login_required
def excluir_projeto(request, pk_prof, pk_grupo, pk_proj, template_name='opta_app/projeto_confirm_delete.html'):
    professor = get_object_or_404(Professor, pk=pk_prof)
    if request.user.professor == professor:
        projeto = get_object_or_404(Projeto, pk=pk_proj)
        if request.method=='POST':
            projeto.delete()
            return redirect('mostrar_grupo', pk_prof, pk_grupo)
        return render(request, template_name, {'object':projeto})
    return redirect('mostrar_professor')

def get_total_vagas():
    total_vagas = 0
    projetos = Projeto.objects.all()
    for projeto in projetos:
        total_vagas += projeto.vagas
    return total_vagas

def filtrar_projetos(curso, palavra_chave):
    projetos = []
    grupos = Grupo.objects.filter(curso=curso)
    for grupo in grupos:
        projeto = Projeto.objects.get(grupo=grupo)
        projetos.append(projeto)
    projetos_2 = list(Projeto.objects.filter(
        Q(titulo__icontains=palavra_chave) |
        Q(subtitulo__icontains=palavra_chave) |
        Q(descricao__icontains=palavra_chave)
    ))
    projetos = list(set(projetos + projetos_2))
    return projetos
