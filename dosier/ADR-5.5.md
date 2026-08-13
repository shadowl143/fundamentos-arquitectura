# ADR 5.5 — Construcción de APIs RESTful avanzadas con Django REST Framework (DRF)
**Contexto:** El endpoint de lista sobre 500 préstamos presenta un costo excesivo de consultas y tamaño de respuesta al serializar relaciones anidadas.
**Opciones:** A = mantener la respuesta anidada sin optimización | B = optimizar con `select_related`, usar serializer plano y activar paginación
**Criterio:** Queries por petición y bytes de respuesta sobre el mismo volumen de 500 filas.
**Evidencia:** Se midieron 500 filas en tres configuraciones: anidado sin optimizar, anidado optimizado y plano; con paginación disminuyeron los bytes y el número de consultas por respuesta (log en `sql.log`).
**Decisión:** B, porque entrega menos queries y respuestas más pequeñas, mejorando la eficiencia del endpoint.
**Consecuencias:** El cliente debe adaptarse al contrato paginado y consumir `results`, `count`, `next` y `previous`.
**Me haría cambiar de opinión:** Si la compatibilidad con consumidores existentes fuera más importante que la optimización o si la paginación no redujera el costo observado.