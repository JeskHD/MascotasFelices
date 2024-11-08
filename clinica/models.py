from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=255, blank=True, null=True)  # Agregar esta línea si necesitas el campo

    def __str__(self):
        return self.nombre
        
class Mascota(models.Model):
    nombre = models.CharField(max_length=255)
    especie = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    edad = models.IntegerField()
    cliente = models.ForeignKey(Cliente, related_name="mascotas", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} ({self.especie}) - {self.cliente.nombre}"

class HistorialMedico(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name='historiales')
    fecha_visita = models.DateField()
    descripcion = models.TextField()

    def __str__(self):
        return f"Visita de {self.mascota.nombre} el {self.fecha_visita}"



