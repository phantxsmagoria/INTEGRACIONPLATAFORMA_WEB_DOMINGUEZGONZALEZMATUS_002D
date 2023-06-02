from django.shortcuts import render
from mi_app.models import Sede, Escuela, Carrera, Docente, Asignatura, Disponibilidad

def index(request):
    sedes = Sede.objects.all()
    escuelas = Escuela.objects.all()
    carreras = Carrera.objects.all()
    docentes = Docente.objects.all()
    asignaturas = Asignatura.objects.all()
    salas_disponibles = Disponibilidad.objects.all()

    context = {
        'sedes': sedes,
        'escuelas': escuelas,
        'carreras': carreras,
        'docentes': docentes,
        'asignaturas': asignaturas,
        'salas_disponibles': salas_disponibles
    }

    return render(request, 'mi_app/index.html', context)
