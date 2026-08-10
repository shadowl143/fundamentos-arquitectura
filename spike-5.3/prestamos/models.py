from django.db import models


class Herramienta(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Prestamo(models.Model):
    herramienta = models.ForeignKey(
        Herramienta,
        on_delete=models.CASCADE
    )
    solicitante = models.CharField(max_length=100)
    fecha_prestamo = models.DateField()
    dias = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.solicitante} - {self.herramienta.nombre}"