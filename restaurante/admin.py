from django.contrib import admin
from .models import Cliente, Prato, Restaurante, Reserva

admin.site.register(Cliente)
admin.site.register(Prato)
admin.site.register(Restaurante)
admin.site.register(Reserva)