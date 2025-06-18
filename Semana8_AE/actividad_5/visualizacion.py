import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Importamos las funciones de los otros archivos
from representacion_binaria import algoritmo_genetico as alg_binaria, decodificar_cromosoma as decodificar_binario
from representacion_permutacional import algoritmo_genetico as alg_permutacional, decodificar_cromosoma as decodificar_permutacional
from representacion_real import algoritmo_genetico as alg_real, decodificar_cromosoma as decodificar_real

# Función para graficar la evolución del fitness
def graficar_evolucion_fitness(historial_binario, historial_permutacional, historial_real):
    plt.figure(figsize=(10, 6))
    
    plt.plot(historial_binario, label='Binaria', color='blue')
    plt.plot(historial_permutacional, label='Permutacional', color='green')
    plt.plot(historial_real, label='Real', color='red')
    
    plt.title('Evolución del Fitness por Generación')
    plt.xlabel('Generaciones')
    plt.ylabel('Fitness')
    plt.legend()
    plt.grid(True)
    plt.show()

# Función para mostrar histograma de las notas por examen
def mostrar_histograma():
    df = pd.read_csv('../notas_1u.csv')
    notas = df['Nota'].tolist()

    plt.figure(figsize=(10, 6))
    
    plt.hist(notas[:13], bins=10, alpha=0.7, label='Examen A')
    plt.hist(notas[13:26], bins=10, alpha=0.7, label='Examen B')
    plt.hist(notas[26:], bins=10, alpha=0.7, label='Examen C')
    
    plt.title('Distribución de Notas por Examen')
    plt.xlabel('Nota')
    plt.ylabel('Número de Alumnos')
    plt.legend()
    plt.grid(True)
    plt.show()

# Función para comparar las distribuciones de las 3 representaciones
def comparar_distribuciones():
    # Ejecutamos los algoritmos y obtenemos las distribuciones de alumnos
    mejor_solucion_binaria = alg_binaria(generaciones=100, tam_poblacion=50)
    mejor_solucion_permutacional, historial_permutacional = alg_permutacional(generaciones=50, tam_poblacion=30)
    mejor_solucion_real = alg_real(generaciones=150, tam_poblacion=100)

    # Decodificar las asignaciones de cada algoritmo
    asignaciones_binarias = decodificar_binario(mejor_solucion_binaria)
    asignaciones_permutacionales = decodificar_permutacional(mejor_solucion_permutacional)
    asignaciones_reales = decodificar_real(mejor_solucion_real)

    # Extraemos las notas de cada examen para cada representación
    df = pd.read_csv('../notas_1u.csv')
    notas = df['Nota'].tolist()
    
    notas_binarias = {examen: [notas[i] for i in asignaciones_binarias[examen]] for examen in ['A', 'B', 'C']}
    notas_permutacionales = {examen: [notas[i] for i in asignaciones_permutacionales[examen]] for examen in ['A', 'B', 'C']}
    notas_reales = {examen: [notas[i] for i in asignaciones_reales[examen]] for examen in ['A', 'B', 'C']}

    # Graficamos las distribuciones de cada representación
    plt.figure(figsize=(15, 6))

    # Binaria
    plt.subplot(1, 3, 1)
    plt.hist(notas_binarias['A'], bins=10, alpha=0.7, label='Examen A')
    plt.hist(notas_binarias['B'], bins=10, alpha=0.7, label='Examen B')
    plt.hist(notas_binarias['C'], bins=10, alpha=0.7, label='Examen C')
    plt.title('Distribución Binaria')
    plt.xlabel('Nota')
    plt.ylabel('Número de Alumnos')
    plt.legend()

    # Permutacional
    plt.subplot(1, 3, 2)
    plt.hist(notas_permutacionales['A'], bins=10, alpha=0.7, label='Examen A')
    plt.hist(notas_permutacionales['B'], bins=10, alpha=0.7, label='Examen B')
    plt.hist(notas_permutacionales['C'], bins=10, alpha=0.7, label='Examen C')
    plt.title('Distribución Permutacional')
    plt.xlabel('Nota')
    plt.ylabel('Número de Alumnos')
    plt.legend()

    # Real
    plt.subplot(1, 3, 3)
    plt.hist(notas_reales['A'], bins=10, alpha=0.7, label='Examen A')
    plt.hist(notas_reales['B'], bins=10, alpha=0.7, label='Examen B')
    plt.hist(notas_reales['C'], bins=10, alpha=0.7, label='Examen C')
    plt.title('Distribución Real')
    plt.xlabel('Nota')
    plt.ylabel('Número de Alumnos')
    plt.legend()

    plt.tight_layout()
    plt.show()

# Función principal para ejecutar las gráficas
def main():
    # Ejecutamos los algoritmos y obtenemos los históricos de fitness
    mejor_solucion_binaria = alg_binaria(generaciones=100, tam_poblacion=50)
    mejor_solucion_permutacional, historial_permutacional = alg_permutacional(generaciones=50, tam_poblacion=30)
    mejor_solucion_real = alg_real(generaciones=150, tam_poblacion=100)

    # Graficamos la evolución del fitness
    graficar_evolucion_fitness(mejor_solucion_binaria, historial_permutacional, mejor_solucion_real)

    # Mostrar el histograma de notas por examen
    mostrar_histograma()

    # Comparar las distribuciones de las 3 representaciones
    comparar_distribuciones()

# Ejecutar la función principal
if __name__ == "__main__":
    main()
