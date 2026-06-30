from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Ator(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self): return self.nome

class Filme(models.Model):
    titulo = models.CharField(max_length=200)
    data_lancamento = models.DateField()
    pais = models.CharField(max_length=100)
    atores = models.ManyToManyField(Ator, related_name='filmes', blank=True)
    def __str__(self): return self.titulo

class Utilizador(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self): return self.nome

class Classificacao(models.Model):
    nota = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE, related_name='classificacoes')
    utilizador = models.ForeignKey(Utilizador, on_delete=models.CASCADE, related_name='classificacoes')