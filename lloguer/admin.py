from django.contrib import admin
from .models import Automobil

class AutomobilAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'marca', 'model')

admin.site.register(Automobil, AutomobilAdmin)
