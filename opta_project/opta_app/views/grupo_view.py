from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from ..models import Grupo, Professor, ProfessorGrupo
from ..forms import GrupoForm

@login_required
def listar_grupo(request, template_name='opta_app/lista_grupo.html'):
    grupos = Grupo.objects.all()
    data = {}
    data['object_list'] = grupos
    return render(request, template_name, data)

@login_required
def criar_grupo(request, template_name='opta_app/form_grupo.html'):
    professor = Professor.objects.get(user_id=request.user.id)
    form = GrupoForm(request.POST or None)
    if form.is_valid():
        grupo = form.save()
        relacionamento = ProfessorGrupo.objects.create(professor_id=professor.id, grupo_id=grupo.pk)
        return redirect('mostrar_professor')
    return render(request, template_name, {'form':form})

@login_required
def atualizar_grupo(request, pk, template_name='opta_app/form_grupo.html'):
    grupo = get_object_or_404(Grupo, pk=pk)
    form = GrupoForm(request.POST or None, instance=grupo)
    if form.is_valid():
        form.save()
        return redirect('mostrar_professor')
    return render(request, template_name, {'form':form})

@login_required
def excluir_grupo(request, pk, template_name='opta_app/grupo_confirm_delete.html'):
    grupo = get_object_or_404(Grupo, pk=pk)
    if request.method=='POST':
        grupo.delete()
        return redirect('mostrar_professor')
    return render(request, template_name, {'object':grupo})
