# ADR 5.1 — Fundamentos de Arquitectura Web, Protocolos HTTP/HTTPS y WSGI/ASGI
**Contexto:** Elegir la interfaz de servidor (WSGI vs ASGI) para una API que debe manejar múltiples peticiones concurrentes sin bloquearse cuando hay operaciones de espera (I/O).
**Opciones:** A = WSGI (modelo síncrono tradicional con Gunicorn)  | B =  ASGI (modelo asíncrono con Uvicorn/FastAPI)
**Criterio:** Capacidad de manejar concurrencia sin bloqueo y número de peticiones atendidas mientras una request está en espera (medido con pruebas de carga concurrentes).
**Evidencia:** En pruebas con 20 peticiones concurrentes a un endpoint con `sleep(5)` ejecutado 3 veces.
**Decisión:** ASGI es mas rapidos.

1. 2026-08-10T11:12:09.571533 MX-30923-T14G2 Windows-11-10.0.26200-SP0
http://127.0.0.1:8001/lento completadas: 20 en 1.03 s
http://127.0.0.1:8002/lento/asgi completadas: 0 en 0.59 s

2. 2026-08-10T11:12:09.571533 MX-30923-T14G2 Windows-11-10.0.26200-SP0
http://127.0.0.1:8001/lento completadas: 20 en 1.03 s
http://127.0.0.1:8002/lento/asgi completadas: 0 en 0.59 s

3. 2026-08-10T11:12:28.549952 MX-30923-T14G2 Windows-11-10.0.26200-SP0
http://127.0.0.1:8001/lento completadas: 20 en 0.84 s
http://127.0.0.1:8002/lento/asgi completadas: 0 en 0.4 s

**Consecuencias:** Se adopta programación asíncrona (`async/await`), Mayor complejidad conceptual, Se requiere servidor compatible (Uvicorn/Hypercorn).
**Me haría cambiar de opinión:** Si el sistema fuera estrictamente CPU-bound, sin operaciones I/O concurrentes, o si las pruebas demostraran que el overhead de ASGI supera sus beneficios bajo nuestra carga real.