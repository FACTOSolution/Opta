from django.shortcuts import render, redirect, get_object_or_404
from ..models import Projeto
from ..forms import ProjetoForm

def listar_projeto(request, template_name='opta_app/lista_projeto.html'):
    projetos = Projeto.objects.all()
    data = {}
    data['object_list'] = projetos
    return render(request, template_name, data)

def criar_projeto(request, template_name='opta_app/form_projeto.html'):
    form = ProjetoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_projeto')
    return render(request, template_name, {'form':form})

def atualizar_projeto(request, pk, template_name='opta_app/form_projeto.html'):
    projeto = get_object_or_404(Projeto, pk=pk)
    form = ProjetoForm(request.POST or None, instance=projeto)
    if form.is_valid():
        form.save()
        return redirect('listar_projeto')
    return render(request, template_name, {'form':form})

def excluir_projeto(request, pk, template_name='opta_app/projeto_confirm_delete.html'):
    projeto = get_object_or_404(Projeto, pk=pk)
    if request.method=='POST':
        projeto.delete()
        return redirect('listar_projeto')
    return render(request, template_name, {'object':projeto})
