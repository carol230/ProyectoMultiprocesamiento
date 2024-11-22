import numpy as np
import matplotlib.pyplot as plt
from time import time
import psutil
from multiprocessing import Pool, cpu_count
import matplotlib
import sys

# Cambiar el backend para evitar problemas con TkAgg
matplotlib.use('Agg')

# Aumentar el límite de recursión si es necesario
sys.setrecursionlimit(2000)

# Parámetros de la imagen
WIDTH = 1000
HEIGHT = 800
MAX_ITER = 1000
C = complex(-0.7, 0.27015)

def julia_recursive(z, c, max_iter, current_iter=0):
    """Calcula recursivamente el número de iteraciones para un punto del conjunto de Julia."""
    if abs(z) > 2 or current_iter >= max_iter:
        return current_iter
    if current_iter >= 2000:  # Límite interno para evitar recursión profunda
        while current_iter < max_iter and abs(z) <= 2:
            z = z * z + c
            current_iter += 1
        return current_iter
    return julia_recursive(z * z + c, c, max_iter, current_iter + 1)

def compute_row(y):
    """Calcula una fila de la imagen del fractal de Julia."""
    row = np.zeros(WIDTH)
    for x in range(WIDTH):
        re = 3.5 * (x / WIDTH - 0.5)
        im = 2.0 * (y / HEIGHT - 0.5)
        z = complex(re, im)
        row[x] = julia_recursive(z, C, MAX_ITER)
    return row

def generate_julia_parallel():
    with Pool(processes=cpu_count()) as pool:
        image = pool.map(compute_row, range(HEIGHT))
    return np.array(image)

if __name__ == "__main__":
    process = psutil.Process()

    # Llamada inicial para establecer un punto de referencia
    process.cpu_percent()

    # Medir recursos antes de ejecutar el programa
    mem_usage_before = process.memory_info().rss / (1024 ** 2)

    start_time = time()
    image = generate_julia_parallel()
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
    plt.savefig("julia_fractal_parallel_recursive_safe.png", dpi=300)
    print("Imagen guardada como 'julia_fractal_parallel_recursive_safe.png'")