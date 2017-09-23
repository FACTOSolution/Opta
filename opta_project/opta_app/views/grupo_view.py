from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from ..models import Grupo, Professor, ProfessorGrupo, Projeto
from ..forms import GrupoForm, AdicionarProfessorAoGrupoForm

@login_required
def mostrar_grupo(request, pk_prof, pk_grupo, template_name='opta_app/detalhe_grupo.html'):
    professor = get_object_or_404(Professor, pk=pk_prof)
    if request.user.professor == professor:
        grupo = get_object_or_404(Grupo, pk=pk_grupo)
        projetos = Projeto.objects.filter(grupo_id=pk_grupo, professor_id=request.user.id)
        data = {}
        data['pk_prof'] = pk_prof
        data['grupo'] = grupo
        data['projetos'] = projetos
        return render(request, template_name, data)
    return redirect('mostrar_professor')

@login_required
def listar_grupo(request, template_name='opta_app/lista_grupo.html'):
    grupos = Grupo.objects.all()
    data = {}
    data['object_list'] = grupos
    return render(request, template_name, data)

@login_required
def criar_grupo(request, pk_prof, template_name='opta_app/form_grupo.html'):
    professor = get_object_or_404(Professor, pk=pk_prof)
    if request.user.professor == professor:
        form = GrupoForm(request.POST or None)
        if form.is_valid():
            grupo = form.save()
            relacionamento = ProfessorGrupo.objects.create(professor_id=professor.id, grupo_id=grupo.pk)
            return redirect('mostrar_professor')
        return render(request, template_name, {'form':form})
    return redirect('mostrar_professor')

@login_required
def atualizar_grupo(request, pk_prof, pk_grupo, template_name='opta_app/form_grupo.html'):
    professor = get_object_or_404(Professor, pk=pk_prof)
    if request.user.professor == professor:
        grupo = get_object_or_404(Grupo, pk=pk_grupo)
        form = GrupoForm(request.POST or None, instance=grupo)
        if form.is_valid():
            form.save()
            return redirect('mostrar_professor')
        return render(request, template_name, {'form':form})
    return redirect('mostrar_professor')

@login_required
def excluir_grupo(request, pk_prof, pk_grupo, template_name='opta_app/grupo_confirm_delete.html'):
    professor = get_object_or_404(Professor, pk=pk_prof)
    if request.user.professor == professor:
        grupo = get_object_or_404(Grupo, pk=pk_grupo)
        if request.method=='POST':
            grupo.delete()
            return redirect('mostrar_professor')
        return render(request, template_name, {'object':grupo})
    return redirect('mostrar_professor')

@login_required
def adicionar_professor_ao_grupo(request, pk_prof, pk_grupo, template_name='opta_app/form_grupo.html'):
    professor = get_object_or_404(Professor, pk=pk_prof)
    if request.user.professor == professor:
        grupo = get_object_or_404(Grupo, pk=pk_grupo)
        form = AdicionarProfessorAoGrupoForm(request.POST or None)
        if form.is_valid():
            grupo_obj = form.cleaned_data
            professor_username = grupo_obj['professor']
            user = get_object_or_404(User, username=professor_username)
            relacionamento = ProfessorGrupo.objects.create(professor_id=user.professor.id, grupo_id=grupo.pk)
            return redirect('mostrar_professor')
        return render(request, template_name, {'form':form})
    return redirect('mostrar_professor')
