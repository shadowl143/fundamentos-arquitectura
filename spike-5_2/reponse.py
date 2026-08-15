# payloads.py (adapta los campos a TU recurso)
import datetime, platform, httpx
print(datetime.datetime.now().isoformat(), platform.node(), platform.platform())

CASOS = {
"1_ok": {"herramienta_id": 1, "solicitante": "Ana Ruiz", "fecha_prestamo": "2026-08-07", "dias": 3},
"2_falta_campo": {"herramienta_id": 1, "solicitante": "Ana Ruiz", "dias": 3},
"3_tipo_malo": {"herramienta_id": "uno", "solicitante": "Ana Ruiz", "fecha_prestamo": "2026-08-07", "dias": 3},
"4_fuera_rango": {"herramienta_id": 1, "solicitante": "Ana Ruiz", "fecha_prestamo": "2026-08-07", "dias": -5},
"5_campo_extra": {"herramienta_id": 1, "solicitante": "Ana Ruiz", "fecha_prestamo": "2026-08-07", "dias": 3, "admin": True},
"6_fecha_basura": {"herramienta_id": 1, "solicitante": "Ana Ruiz", "fecha_prestamo": "ayer", "dias": 3},
}

for base in ("http://127.0.0.1:8002", "http://127.0.0.1:8001"):
    for nombre, cuerpo in CASOS.items():
        r = httpx.post(base + "/api/prestamos", json=cuerpo)
        print(base, nombre, r.status_code, r.text[:120])