from django.core.management.base import BaseCommand
from django.db import connection

import datetime, platform
print(datetime.datetime.now().isoformat(), platform.node(), platform.platform())

class Command(BaseCommand):
    help = 'Mide estadísticas SQL de la tabla prestamos'

    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) AS total FROM prestamos;")
            total = cursor.fetchone()[0]

            cursor.execute("""
                SELECT COUNT(*) AS con_dato
                FROM prestamos
                WHERE solicitante_nombre IS NOT NULL AND solicitante_nombre <> '';
            """)
            con_dato = cursor.fetchone()[0]

            cursor.execute("""
                SELECT COUNT(*) AS huerfanos
                FROM prestamos p
                LEFT JOIN herramientas h ON h.id = p.herramienta_id
                WHERE h.id IS NULL;
            """)
            huerfanos = cursor.fetchone()[0]

        self.stdout.write(f"total={total}")
        self.stdout.write(f"con_dato={con_dato}")
        self.stdout.write(f"huerfanos={huerfanos}")