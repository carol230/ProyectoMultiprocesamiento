import numpy as np
import matplotlib.pyplot as plt
from time import time
import psutil
import matplotlib
import sys

# Cambiar el backend para evitar problemas con TkAgg
matplotlib.use('Agg')
sys.setrecursionlimit(2000)

# Parámetros de la imagen
WIDTH = 1000
HEIGHT = 800
MAX_ITER = 1000
C = complex(-0.7, 0.27015)  # Número complejo fijo para el conjunto de Julia

def julia_recursive(z, c, max_iter, current_iter=0):
    """Calcula recursivamente el número de iteraciones, limitando la profundidad."""
    if abs(z) > 2 or current_iter >= max_iter:
        return current_iter
    if current_iter >= 2000:  # Límite interno para evitar recursión profunda
        while current_iter < max_iter and abs(z) <= 2:
            z = z * z + c
            current_iter += 1
        return current_iter
    return julia_recursive(z * z + c, c, max_iter, current_iter + 1)


def generate_julia(width, height, max_iter, c):
    image = np.zeros((height, width))
    for x in range(width):
        for y in range(height):
            # Mapeo de coordenadas al plano complejo
            re = 3.5 * (x / width - 0.5)
            im = 2.0 * (y / height - 0.5)
            z = complex(re, im)
            image[y, x] = julia_recursive(z, c, max_iter)
    return image

if __name__ == "__main__":
    process = psutil.Process()

    # Medir recursos antes de ejecutar el programa
    process.cpu_percent()
    mem_usage_before = process.memory_info().rss / (1024 ** 2)

    start_time = time()
    image = generate_julia(WIDTH, HEIGHT, MAX_ITER, C)
    end_time = time()

    # Medir recursos después de ejecutar el programa
    cpu_usage_after = process.cpu_percent(interval=0.1)
    mem_usage_after = process.memory_info().rss / (1024 ** 2)

    # Mostrar resultados
    print(f"Tiempo de ejecución: {end_time - start_time:.2f} segundos")
    print(f"Uso de CPU del proceso: {cpu_usage_after:.2f}%")
    print(f"Uso de memoria antes: {mem_usage_before:.2f} MB")
    print(f"Uso de memoria después: {mem_usage_after:.2f} MB")

    # Ajustar los valores de la imagen para mejorar la visualización
    image = np.log(image + 1)

    # Generar la imagen con colores ajustados
    plt.imshow(image, cmap="plasma", extent=[-2, 2, -2, 2])
    plt.colorbar()
    plt.savefig("julia_fractal_recursive.png", dpi=300)
    print("Imagen guardada como 'julia_fractal_recursive.png'")
