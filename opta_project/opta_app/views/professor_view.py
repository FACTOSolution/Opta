from django.shortcuts import render, redirect, get_object_or_404
from ..models.professor import Professor
from ..forms import ProfessorForm

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

def atualizar_professor(request, pk, template_name='opta_app/form_professor.html'):
    professor = get_object_or_404(Professor, pk=pk)
    form = ProfessorForm(request.POST or None, instance=professor)
    if form.is_valid():
        form.save()
        return redirect('listar_professor')
    return render(request, template_name, {'form':form})

def excluir_professor(request, pk, template_name='opta_app/professor_confirm_delete.html'):
    professor = get_object_or_404(Professor, pk=pk)
    if request.method=='POST':
        professor.delete()
        return redirect('listar_professor')
    return render(request, template_name, {'object':professor})
