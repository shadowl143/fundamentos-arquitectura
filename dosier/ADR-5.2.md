# ADR 5.1 — Desarrollo de Microservicios y APIs de alto rendimiento con FastAPI
**Contexto:** Medir lo casos que se pueden atrapar.
**Opciones:** ASGI (modelo asíncrono con Uvicorn/FastAPI)
**Criterio:** Se realizan 5 casos diferentes aportando diferentes datos.
**Evidencia:** 
## Tabla 6×2: Atrapado / No atrapado

| Caso | Puerto 8002 | Puerto 8001 |
|--------|--------|--------|
| 1_ok | No atrapado (201) | No atrapado (201) |
| 2_falta_campo | Atrapado (422) | Atrapado (422) |
| 3_tipo_malo | Atrapado (422) | Atrapado (422) |
| 4_fuera_rango | Atrapado (422) | Atrapado (422) |
| 5_campo_extra | No atrapado (201) | No atrapado (201) |
| 6_fecha_basura | Atrapado (422) | Atrapado (422) |

## Tabla 6×2: Códigos de estado

| Caso | Puerto 8002 | Puerto 8001 |
|------|------------|------------|
| 1_ok | 201 | 201 |
| 2_falta_campo | 422 | 422 |
| 3_tipo_malo | 422 | 422 |
| 4_fuera_rango | 422 | 422 |
| 5_campo_extra | 201 | 201 |
| 6_fecha_basura | 422 | 422 |

## logs
2026-08-10T11:34:49.426225 MX-30923-T14G2 Windows-11-10.0.26200-SP0
- http://127.0.0.1:8002 1_ok 201 {"herramienta_id":1,"solicitante":"Ana Ruiz","fecha_prestamo":"2026-08-07","dias":3}
- http://127.0.0.1:8002 2_falta_campo 422 {"detail":[{"type":"missing","loc":["body","fecha_prestamo"],"msg":"Field required","input":{"herramienta_id":1,"solicit
- http://127.0.0.1:8002 3_tipo_malo 422 {"detail":[{"type":"int_parsing","loc":["body","herramienta_id"],"msg":"Input should be a valid integer, unable to parse
- http://127.0.0.1:8002 4_fuera_rango 422 {"detail":[{"type":"greater_than","loc":["body","dias"],"msg":"Input should be greater than 0","input":-5,"ctx":{"gt":0}
- http://127.0.0.1:8002 5_campo_extra 201 {"herramienta_id":1,"solicitante":"Ana Ruiz","fecha_prestamo":"2026-08-07","dias":3}
- http://127.0.0.1:8002 6_fecha_basura 422 {"detail":[{"type":"date_from_datetime_parsing","loc":["body","fecha_prestamo"],"msg":"Input should be a valid date or d
- http://127.0.0.1:8001 1_ok 201 {"herramienta_id":1,"solicitante":"Ana Ruiz","fecha_prestamo":"2026-08-07","dias":3}
- http://127.0.0.1:8001 2_falta_campo 422 {"detail":[{"type":"missing","loc":["body","fecha_prestamo"],"msg":"Field required","input":{"herramienta_id":1,"solicit
- http://127.0.0.1:8001 3_tipo_malo 422 {"detail":[{"type":"int_parsing","loc":["body","herramienta_id"],"msg":"Input should be a valid integer, unable to parse
- http://127.0.0.1:8001 4_fuera_rango 422 {"detail":[{"type":"greater_than","loc":["body","dias"],"msg":"Input should be greater than 0","input":-5,"ctx":{"gt":0}
- http://127.0.0.1:8001 5_campo_extra 201 {"herramienta_id":1,"solicitante":"Ana Ruiz","fecha_prestamo":"2026-08-07","dias":3}
- http://127.0.0.1:8001 6_fecha_basura 422 {"detail":[{"type":"date_from_datetime_parsing","loc":["body","fecha_prestamo"],"msg":"Input should be a valid date or d.

**Decisión:** ASGI es mas rapidos
**Consecuencias:** Ambas implementaciones (puertos 8001 y 8002) muestran el mismo comportamiento.
**Me haría cambiar de opinión:**