from django.contrib import admin
from .models import Investigador, Projeto, Entregavel

admin.site.register(Investigador)
admin.site.register(Projeto)
admin.site.register(Entregavel)