# proyecto integrados modulo 5
El proyecto se define por varios spike cada spike tiene un proceso que se realiza diferentes acciones, en los cuales es necesario ejecutar comandos.

## como probar.
Lo primero es ejecutar el comando `uv async` con esto se van a instalar todas las librearias necesarias y se pueden probar los servicios con los siguientes comandos.

### spike 5.4
- python ./spike-5.4/manage.py cargar_prestamos ~ cargar al azar 500 registros para el uso del api
- python ./spike-5.4/manage.py estadisticas_prestamos ~ realiza unas busquedas para contar los datos huerfanos, cantidad de registros.
- python ./spike-5.4/manage.py metricas ~ por medio de ajustes se mide nuevamente la mterica de las estadisticas de prestamos.

## spike 5.5
- python ./spike-5.5/manage.py medir_prestamos

## spike 5.7
- 