from django.db import models


class Herramienta(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'herramientas'

    def __str__(self):
        return self.nombre


class Prestamo(models.Model):
    id = models.AutoField(primary_key=True)
    solicitante_nombre = models.CharField(max_length=75, blank=True, null=True)
    solicitante_apellido = models.CharField(max_length=75, blank=True, null=True)
    herramienta = models.ForeignKey(
        Herramienta,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='prestamos'
    )
    fecha_prestamo = models.DateField(auto_now_add=True)
    fecha_devolucion = models.DateField(blank=True, null=True)
    estado = models.CharField(max_length=20, default='activo')

    class Meta:
        db_table = 'prestamos'

    def __str__(self):
        return f"Préstamo #{self.id}"
