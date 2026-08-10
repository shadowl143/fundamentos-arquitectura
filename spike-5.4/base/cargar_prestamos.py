import random
from datetime import date, timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone

from models import Herramienta, Prestamo


class Command(BaseCommand):
    help = 'Carga masiva de 500 préstamos con distintas combinaciones'

    def handle(self, *args, **options):
        self.stdout.write('Iniciando carga masiva...')

        # Crear herramientas de ejemplo si no existen
        if Herramienta.objects.count() == 0:
            herramientas = []
            for i in range(1, 21):
                herramienta = Herramienta.objects.create(
                    nombre=f'Herramienta {i}',
                    descripcion=f'Descripción de la herramienta {i}'
                )
                herramientas.append(herramienta)
        else:
            herramientas = list(Herramienta.objects.all())

        nombres = [
            'Juan Pérez', 'María López', 'Carlos Gómez', 'Ana Torres',
            'Pedro Ramírez', 'Lucía Fernández', 'Andrés Ruiz', 'Sofía Castro',
            'Diego Morales', 'Elena Vargas'
        ]

        estados = ['activo', 'devuelto', 'vencido', 'cancelado']

        prestamos_creados = 0

        for i in range(500):
            # 70% con solicitante, 30% vacío/null
            if random.random() < 0.7:
                solicitante = random.choice(nombres)
            else:
                solicitante = random.choice([None, ''])

            # 80% con herramienta, 20% sin herramienta
            if random.random() < 0.8:
                herramienta = random.choice(herramientas)
            else:
                herramienta = None

            # Fechas aleatorias en los últimos 180 días
            dias_atras = random.randint(0, 180)
            fecha_prestamo = timezone.now().date() - timedelta(days=dias_atras)

            # Fecha de devolución opcional
            fecha_devolucion = None
            if random.random() < 0.6:
                fecha_devolucion = fecha_prestamo + timedelta(days=random.randint(1, 30))

            estado = random.choice(estados)

            Prestamo.objects.create(
                solicitante=solicitante,
                herramienta=herramienta,
                fecha_prestamo=fecha_prestamo,
                fecha_devolucion=fecha_devolucion,
                estado=estado
            )
            prestamos_creados += 1

        self.stdout.write(self.style.SUCCESS(f'Se crearon {prestamos_creados} préstamos correctamente.'))