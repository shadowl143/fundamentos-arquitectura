from django.core.management.base import BaseCommand
from django.test import Client
from django.test.utils import CaptureQueriesContext
from django.db import connection
import datetime
import platform


class Command(BaseCommand):
    help = "Mide queries y tamaño de respuesta para los endpoints de préstamos"

    def handle(self, *args, **options):
        cliente = Client()

        urls = [
            "/api/prestamos/nested/",
            "/api/prestamos/nested-optimized/",
            "/api/prestamos/flat/",
            "/api/prestamos/nested-paginated/",
            "/api/prestamos/nested-optimized-paginated/",
            "/api/prestamos/flat-paginated/",
        ]

        print("timestamp:", datetime.datetime.now().isoformat())
        print("node:", platform.node())
        print("platform:", platform.platform())
        print("python:", platform.python_version())
        print("=" * 60)

        for url in urls:
            with CaptureQueriesContext(connection) as ctx:
                response = cliente.get(url)

            print(f"URL: {url}")
            print("queries:", len(ctx.captured_queries))
            print("bytes:", len(response.content))
            print("--- SQL ---")
            for i, q in enumerate(ctx.captured_queries, start=1):
                print(f"{i}. {q['sql']}")
            print("=" * 60)