# votacao/models.py

from django.db import models
from django.contrib.auth.models import User

class Candidato(models.Model):
    """
    Representa um candidato na eleição.
    """
    nome = models.CharField(max_length=100)
    numero = models.IntegerField(unique=True)

    def __str__(self):
        return f"{self.nome} ({self.numero})"

class Voto(models.Model):
    """
    Representa um voto de um eleitor para um candidato.
    O voto é assinado digitalmente para garantir a integridade.
    """
    eleitor = models.ForeignKey(User, on_delete=models.CASCADE)
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
    data_hora = models.DateTimeField(auto_now_add=True)
    assinatura_digital = models.TextField() # Campo para armazenar a assinatura em formato de texto (ex: Base64)

    def __str__(self):
        return f"Voto de {self.eleitor.username} para {self.candidato.nome} em {self.data_hora}"