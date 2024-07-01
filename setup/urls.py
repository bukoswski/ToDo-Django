
from django.contrib import admin
from django.urls import path
from Todos.views import home, cadastro, tarefa

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('cadastro/', cadastro, name='cadastro'),
    path('tarefas', tarefa, name='tarefa')
]
