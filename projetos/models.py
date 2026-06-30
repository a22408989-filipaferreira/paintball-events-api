from django.db import models

class Investigador(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self): return self.nome

class Projeto(models.Model):
    titulo = models.CharField(max_length=150)
    resumo = models.TextField()
    data_inicio = models.DateField()
    coordenador = models.ForeignKey(Investigador, on_delete=models.CASCADE, related_name='projetos_coordenados')
    investigadores = models.ManyToManyField(Investigador, related_name='projetos_associados', blank=True)
    def __str__(self): return self.titulo

class Entregavel(models.Model):
    tipo = models.CharField(max_length=100)
    data_entrega = models.DateField()
    link = models.URLField()
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name='entregaveis')
    def __str__(self): return self.tipo