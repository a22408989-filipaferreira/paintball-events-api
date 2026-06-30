from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self): return self.nome

class Prato(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self): return self.nome

class Restaurante(models.Model):
    nome = models.CharField(max_length=100)
    localizacao = models.CharField(max_length=150)
    capacidade = models.IntegerField()
    menu = models.ManyToManyField(Prato, related_name='restaurantes', blank=True)
    def __str__(self): return self.nome

class Reserva(models.Model):
    data = models.DateField()
    hora = models.TimeField()
    numero_pessoas = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='reservas')
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE, related_name='reservas')