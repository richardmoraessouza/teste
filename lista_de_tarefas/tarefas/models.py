from django.db import models

class Tarefa_usuario(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=1000)