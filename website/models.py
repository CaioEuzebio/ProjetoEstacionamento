from django.db import models


class Contato(models.Model):
    email = models.EmailField()
    nome = models.CharField(max_length=100, blank=False, null=False)
    sobrenome = models.CharField(max_length=100, blank=False, null=False)
    cidade = models.CharField(max_length=100, blank=False, null=False)
    estado = models.CharField(max_length=100, blank=False, null=False)
    mensagem = models.CharField(max_length=100, blank=False, null=False)
    receber_promocoes = models.BooleanField()

    def __str__(self):
        return self.nome





