from django.shortcuts import render, redirect, get_object_or_404
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

def editar(request, id):
    todo = get_object_or_404(Todos, id=id)
    
    if request.method == 'POST':
        todo.tarefa = request.POST.get('tarefa')    
        todo.descricao = request.POST.get('descricao')
        todo.data_entrega = request.POST.get('data_entrega')
        todo.save()
        return redirect("home")
    else:
        return render(request, "editar.html", {"todo": todo})