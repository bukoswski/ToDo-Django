from django.shortcuts import render, redirect
from .models import Todos

def home(request):
    return render(request, "home.html")

def cadastro(request):
    if request.method == 'POST':
        banco = Todos()
        banco.tarefa = request.POST.get('tarefa')
        banco.descricao = request.POST.get('descricao')
        banco.data_entrega = request.POST.get('data_entrega')
        banco.save()
        return redirect ("tarefas")
    else:           
        return render(request, "cadastro.html")

def tarefa(request):
    tarefas = Todos.objects.all()
    return render(request, "tarefas.html", {"tarefas": tarefas})

