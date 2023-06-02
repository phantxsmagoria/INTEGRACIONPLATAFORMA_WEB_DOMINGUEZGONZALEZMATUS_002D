import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "integracionweb.settings")
django.setup()

from mi_app.models import Sede, Escuela, Carrera, Docente, Asignatura, Sala, Disponibilidad

def populate_db():
    # Crear objetos de ejemplo
    sede = Sede.objects.create(nombre='Sede 1')
<<<<<<< HEAD
    escuela = Escuela.objects.create(nombre='Escuela de Informática', sede=sede)
    carrera = Carrera.objects.create(nombre='Ingeniería de Informática', escuela=escuela)
    docente = Docente.objects.create(nombre='Alvaro Lopez', carrera=carrera)
    asignatura = Asignatura.objects.create(nombre='Arquitectura de Información', docente=docente)
    sala = Sala.objects.create(nombre='Sala 1')
    disponibilidad = Disponibilidad.objects.create(sala=sala, asignatura=asignatura, cantidad_disponible=5)
=======
    escuela = Escuela.objects.create(nombre='Escuela 1', sede=sede)
    carrera = Carrera.objects.create(nombre='Carrera 1', escuela=escuela)
    docente = Docente.objects.create(nombre='Docente 1', carrera=carrera)
    asignatura = Asignatura.objects.create(nombre='Filosofía', docente=docente)
    sala = Sala.objects.create(nombre='Sala 1')
    disponibilidad = Disponibilidad.objects.create(sala=sala, asignatura=asignatura, cantidad_disponible=3)
>>>>>>> c199ec28aa949830dc98cd786a8ad3e5f70461fe

if __name__ == '__main__':
    populate_db()