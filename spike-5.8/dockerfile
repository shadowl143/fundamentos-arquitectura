FROM python:3.11-slim

# Evita archivos .pyc y fuerza salida inmediata en logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Directorio de trabajo
WORKDIR /app

# Instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código
COPY . .

# Exponer puerto de Flask
EXPOSE 5000

# Comando por defecto
CMD ["python", "app.py"]