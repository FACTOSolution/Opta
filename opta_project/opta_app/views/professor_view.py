from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from ..models import Professor
from ..forms import UserForm, ProfessorForm

@login_required
def listar_professor(request, template_name='opta_app/lista_professor.html'):
    professores = Professor.objects.all()
    data = {}
    data['object_list'] = professores
    return render(request, template_name, data)

#def criar_professor(request, template_name='opta_app/form_professor.html'):
#    form = ProfileForm(request.POST or None)
#    if form.is_valid():
#        form.save()
#        return redirect('listar_professor')
#    return render(request, template_name, {'form':form})

@login_required
def atualizar_professor(request, pk, template_name='opta_app/form_professor.html'):
    professor = get_object_or_404(Professor, pk=pk)
    user = get_object_or_404(User, pk=professor.user_id)
    user_form = UserForm(request.POST or None, instance=user)
    professor_form = ProfessorForm(request.POST or None, instance=user.professor)
    if user_form.is_valid() and professor_form.is_valid():
        user_form.save()
        professor_form.save()
        return redirect('listar_professor')
    return render(request, template_name, {'user_form': user_form,
        'professor_form': professor_form})

@login_required
def excluir_professor(request, pk, template_name='opta_app/professor_confirm_delete.html'):
    professor = get_object_or_404(Professor, pk=pk)
    if request.method=='POST':
        professor.delete()
        return redirect('listar_professor')
    return render(request, template_name, {'object':professor})
