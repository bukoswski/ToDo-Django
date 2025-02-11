
from django.contrib import admin
from django.urls import path
from Todos.views import home, cadastro, tarefa, editar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('cadastro/', cadastro, name='cadastro'),
    path('tarefas', tarefa, name='tarefa'),
    path('editar/<int:id>/', editar, name='editar')
]
