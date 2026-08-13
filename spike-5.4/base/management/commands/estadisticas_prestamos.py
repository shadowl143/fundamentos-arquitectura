from django.core.management.base import BaseCommand
from django.db.models import Count, Q
from base.models import Prestamo


class Command(BaseCommand):
    help = 'Muestra estadísticas equivalentes a consultas SQL sobre préstamos'

    def handle(self, *args, **options):
        total = Prestamo.objects.count()
        con_dato = Prestamo.objects.filter(
            solicitante_nombre__isnull=False
        ).exclude(
            solicitante_nombre=''
        ).count()

        # Huérfanos: préstamos sin herramienta asociada
        huerfanos = Prestamo.objects.filter(herramienta__isnull=True).count()

        self.stdout.write(f"SELECT COUNT(*) AS total FROM prestamos;")
        self.stdout.write(f"total = {total}\n")

        self.stdout.write(f"SELECT COUNT(*) AS con_dato FROM prestamos WHERE solicitante_nombre IS NOT NULL AND solicitante_nombre <> '';")
        self.stdout.write(f"con_dato = {con_dato}\n")

        self.stdout.write("SELECT COUNT(*) AS huerfanos FROM prestamos p LEFT JOIN herramientas h ON h.id = p.herramienta_id WHERE h.id IS NULL;")
        self.stdout.write(f"huerfanos = {huerfanos}")