from django import forms
from models import Todos

class TodosForm(forms.ModelForm):
    class meta:
        model = Todos
        fields = ['titulo', 'descricao', 'data_entrega']
        