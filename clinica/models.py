from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.nombre

class Mascota(models.Model):
    ESPECIES = (
        ('Perro', 'Perro'),
        ('Gato', 'Gato'),
        ('Ave', 'Ave'),
        ('Otro', 'Otro'),
    )
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=50, choices=ESPECIES)
    raza = models.CharField(max_length=100)
    edad = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='mascotas')

    def __str__(self):
        return self.nombre

class HistorialMedico(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name='historiales')
    fecha_visita = models.DateField()
    descripcion = models.TextField()

    def __str__(self):
        return f"Visita de {self.mascota.nombre} el {self.fecha_visita}"
