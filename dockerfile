# Usa una imagen base ligera de Python
FROM python:3.9-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos necesarios
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Exponer el puerto donde corre la aplicación
# EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "src/main.py"]