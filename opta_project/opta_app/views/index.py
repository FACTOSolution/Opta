from django.shortcuts import render

def mostrar(request):
    return render(request, 'index.html', context={'teste':'Página inicial'})
