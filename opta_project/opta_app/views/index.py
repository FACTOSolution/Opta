from django.shortcuts import render

def mostrar(request):
    return render(request, 'index.html')
