from django.db import models

# Create your models here.
class Sede(models.Model):
    nombre = models.CharField(max_length=100)

class Escuela(models.Model):
    nombre = models.CharField(max_length=100)
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE)

class Carrera(models.Model):
    nombre = models.CharField(max_length=100)
    escuela = models.ForeignKey(Escuela, on_delete=models.CASCADE)

class Docente(models.Model):
    nombre = models.CharField(max_length=100)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)

class Asignatura(models.Model):
    nombre = models.CharField(max_length=100)
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)

class Sala(models.Model):
    nombre = models.CharField(max_length=100)

class Disponibilidad(models.Model):
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    cantidad_disponible = models.PositiveIntegerField()
