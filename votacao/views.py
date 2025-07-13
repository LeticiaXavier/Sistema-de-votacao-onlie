# votacao/views.py

from django.shortcuts import render
from .models import Candidato

def exibir_cedula(request):
    """
    Esta view busca todos os candidatos no banco de dados e
    os envia para o template da cédula de votação.
    """
    candidatos = Candidato.objects.all()
    contexto = {'lista_candidatos': candidatos}
    return render(request, 'votacao/cedula.html', contexto)