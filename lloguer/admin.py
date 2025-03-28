from django.contrib import admin
from .models import Automobil, Reserva

class AutomobilAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'marca', 'model')

admin.site.register(Automobil, AutomobilAdmin)

class ReservaAdmin(admin.ModelAdmin):
    list_display = ('automobil', 'user', 'data_inici', 'data_fi')

admin.site.register(Reserva, ReservaAdmin)