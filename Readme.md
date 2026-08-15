# proyecto integrados modulo 5
El proyecto se define por varios spike cada spike tiene un proceso que se realiza diferentes acciones, en los cuales es necesario ejecutar comandos.

## como probar.
Lo primero es ejecutar el comando `uv async` con esto se van a instalar todas las librearias necesarias y se pueden probar los servicios con los siguientes comandos.
### spike-5_1
- uvicorn spike-5_1.app:app --workers 1 --port 8002
- uvicorn spike-5_1.app:app --workers 1 --port 8001
python spike-5_1/requests.py

### spike-5_2
- uvicorn spike-5_1.app:app --workers 1 --port 8002
- uvicorn spike-5_1.app:app --workers 1 --port 8001
python spike-5_2/reponse.py 

### spike-5.3
Migraciones

### spike 5.4
- python ./spike-5.4/manage.py cargar_prestamos ~ cargar al azar 500 registros para el uso del api
- python ./spike-5.4/manage.py estadisticas_prestamos ~ realiza unas busquedas para contar los datos huerfanos, cantidad de registros.
- python ./spike-5.4/manage.py metricas ~ por medio de ajustes se mide nuevamente la mterica de las estadisticas de prestamos.

## spike 5.5
- python ./spike-5.5/manage.py medir_prestamos

## spike 5.6
-  uvicorn spike-5_6.app:app --workers 1 --port 8001

## spike 5.7
- ingresar a la carpeta spike-5.7
- pytest -q

## spike 5.8
- ingresar a la carpeta spike-5.8
- pytest -q