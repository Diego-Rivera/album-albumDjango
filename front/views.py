from django.shortcuts import render
from .models import Foto

# Create your views here.
def Index(request):
    fotos = Foto.objects.all()
    datos ={'fotos': fotos} #par ordenado de atributo y valor que se van a pasar a la vista
    return render(request, 'index.html', datos)