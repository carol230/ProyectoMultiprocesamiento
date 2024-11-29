# Proyecto: Fractal de Julia en Python

Este proyecto genera un fractal de Julia utilizando Python. A continuación, se explica cómo descargar y ejecutar el código en una computadora para visualizar el fractal generado.

## Requisitos previos
- Tener instalado [Python 3](https://www.python.org/downloads/) en su computadora.
- Tener instalado [Visual Studio Code (VSCode)](https://code.visualstudio.com/download) para visualizar la imagen generada.

## Instrucciones para ejecutar el programa

1. **Descargar el proyecto desde Git**
   - Clona o descarga los archivos del repositorio desde GitHub. Puedes hacerlo ejecutando el siguiente comando en PowerShell (asegúrate de estar en la ubicación donde deseas descargar el proyecto):
     ```
     git clone <URL_DEL_REPOSITORIO>
     ```
   - Alternativamente, puedes descargar el repositorio como un archivo ZIP, extraer el contenido y guardarlo en una carpeta.

2. **Abrir PowerShell y navegar a la carpeta del proyecto**
   - Abre PowerShell y utiliza el comando `cd` para navegar a la carpeta donde descargaste los archivos del proyecto. Por ejemplo:
     ```
     cd 'D:\ruta\donde\descargaste\el\proyecto'
     ```

3. **Ejecutar el código**
   - Una vez dentro de la carpeta del proyecto, ejecuta el siguiente comando para correr el programa que genera el fractal de Julia:
     ```
     python fractal_julia_secuencial.py
     ```
     ```
     python fractal_julia_parallel.py
     ```
   - El programa calculará el fractal y generará una imagen en la misma carpeta donde está el código. La ejecución puede tomar algunos segundos, y al finalizar verás un mensaje indicando el tiempo de ejecución.

4. **Visualizar la imagen generada**
   - Para ver la imagen generada, abre la carpeta del proyecto con Visual Studio Code.
   - Busca el archivo de imagen (por ejemplo, `fractal_julia.png`) y ábrelo desde el panel lateral de VSCode para visualizar el fractal.

## Notas adicionales
- Si tienes problemas al ejecutar el programa, asegúrate de tener correctamente instalado Python y configurada la variable de entorno `PATH` para poder ejecutar `python` desde la terminal.
- Puedes modificar los parámetros del código para generar diferentes versiones del fractal de Julia. Esto se puede hacer editando el archivo `fractal_julia_secuencial.py` con cualquier editor de texto como VSCode.
