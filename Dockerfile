# Usa una imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos necesarios en el contenedor
COPY requirements.txt /app/requirements.txt
COPY . /app

# Actualizar pip
RUN pip install --upgrade pip

# Instala las dependencias del archivo requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto 5000 para acceder a la aplicación
EXPOSE 5000

# Comando para ejecutar la aplicación Flask
CMD ["python", "app.py"]

