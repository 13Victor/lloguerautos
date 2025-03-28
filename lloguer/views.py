from django.shortcuts import render
from .models import Automobil

def listar_automoviles(request):
    automoviles = Automobil.objects.all()
    return render(request, 'lloguer/autos_list.html', {'automoviles': automoviles})
