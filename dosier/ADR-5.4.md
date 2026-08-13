# ADR 5.1 — Modelado de Datos, Migraciones y Mapeo Objeto-Relacional (ORM)
**Contexto:** Manejar migraciones con django 
**Opciones:** manejo de migraciones utilizando django.
**Criterio:** Generar una base de datos y por medio de migraciones alterarla 
**Evidencia:** 
![alt text](<files/carga masiva.png>)
![alt text](<files/despues del ajuste.png>)
![alt text](<files/migraciones caso A.png>)
**Decisión:**  Las migraciones son una buena oportunidad de agilizar el proceso ya que por un modelo de python puedes generar la base de datos sin necesidad de utilizar otra herramienta que ayude
**Consecuencias:** Genera migraciones sin embargo esta casada con el luenguaje lo que limita el uso de otro para migrar la base de datos.
**Me haría cambiar de opinión:** Si es necesario cambiar el lenguaje de programación a diferentes motores.