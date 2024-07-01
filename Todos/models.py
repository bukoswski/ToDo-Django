from django.db import models


class Todos(models.Model):
    tarefa = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    data_entrega = models.DateTimeField(null=False)
    entrega = models.BooleanField(default=False)

def __str__(self):
    return self.tarefa



