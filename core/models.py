from django.db import models
import math


class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

    

class Marca(models.Model):
   nomemarca = models.CharField(max_length=50)

   def __str__(self):
       return self.nomemarca





class Veiculo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    placa = models.CharField(max_length=7)
    cor = models.CharField(max_length=15)
    proprietario = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    modelo = models.CharField(max_length=50)
    observacoes = models.TextField()
   
    def __str__(self):
        return self.marca.nomemarca + ' - ' + self.placa



class Parametros(models.Model):
    valor_hora = models.DecimalField(max_digits=5, decimal_places=2)
    valor_mes = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return 'Parametros Gerais'




class MovRotativo(models.Model):
    checkin = models.DateTimeField(auto_now=False)
    checkout = models.DateTimeField(auto_now=False, blank=True, null=True)
    valor_hora = models.DecimalField(max_digits=5, decimal_places=2)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    pago = models.BooleanField(default=False)

    def horas_total(self):
        return math.ceil((self.checkout - self.checkin).total_seconds() / 3600)


    def total(self):
        return self.valor_hora * self.horas_total()

    def __str__(self):
        return self.veiculo.placa


class Mensalista(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    inicio = models.DateField()
    valor_mes = models.DecimalField(max_digits=5, decimal_places=2)


    def __str__(self):
        return str(self.veiculo) + ' - ' + str(self.inicio)


class MovMensalista(models.Model):
    mensalista = models.ForeignKey(Mensalista, on_delete=models.CASCADE)
    datapagamento = models.DateField()
    total = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return str(self.mensalista) + ' - ' + str(self.total)