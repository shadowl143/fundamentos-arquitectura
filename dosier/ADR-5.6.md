# ADR 5.6 — Preferir sesión del servidor para credenciales revocables de acceso sensible
**Contexto:** El endpoint sensible requiere denegar acceso inmediatamente tras logout y evitar que una credencial robada siga funcionando.
**Opciones:** A = sesión del servidor | B = JWT firmado sin estado
**Criterio:** Códigos HTTP en la batería de 7 casos, tiempo de acceso válido tras logout y respuesta ante token manipulado/autorización cruzada.
**Evidencia:** La sesión permitió revocación inmediata o en __ s; el JWT siguió aceptándose durante __ s hasta expirar; autorización cruzada devolvió __; token manipulado devolvió __.
**Decisión:** A, porque permite cortar acceso tras cierre de sesión con menor ventana de riesgo residual.
**Consecuencias:** Acepto mantener estado en servidor y gestionar almacenamiento de sesión, con más costo operativo que JWT.
**Me haría cambiar de opinión:** Si el JWT con expiración corta y revocación demostrara igual o mejor revocabilidad sin aumentar la complejidad del cliente o del despliegue.