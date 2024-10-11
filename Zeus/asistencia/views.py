from django.shortcuts import render
from django.http import HttpResponse
from .models import estudiante

# Aqui tengo mis Vistas o Views
#def inicio(request):
#    return HttpResponse("Bienvenidos a Zeus Asistencia")
def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def servicios(request):
    return render(request, 'paginas/servicios.html')

def contactenos(request):
    return render(request, 'paginas/contactenos.html')

def estudiantes(request):
    estudiantes = estudiante.objects.all()
    return render(request, 'estudiantes/index.html', {'estudiantes': estudiantes})

def crear(request):
    return render(request, 'estudiantes/crear.html')

def editar(request):
    return render(request, 'estudiantes/editar.html')