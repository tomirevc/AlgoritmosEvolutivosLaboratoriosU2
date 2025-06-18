# SEMANA 7
Este dashboard interactivo se crea con Flask y Plotly para visualizar y analizar las notas de los estudiantes de un examen. A través de una interfaz web, el usuario puede ver diversos gráficos y estadísticas descriptivas relacionadas con el rendimiento de los estudiantes, tanto de manera general como por tipo de examen. Asi mismo se incluye la versión usando las librerias de matplot clásicas.

![Image](https://github.com/user-attachments/assets/b6307353-728e-4dac-91e2-ab49000cf0dd)


# SEMANA 8

## ✅ Actividad 1: Análisis Comparativo
Ejecuta los tres programas y compara los resultados
Documenta tus observaciones en un archivo analisis.txt

### 🔷 ¿Cuál representación logra mejor equilibrio entre los grupos?

### 🔷 ¿Cuál converge más rápido? (observa las generaciones)

## ✅ Actividad 2: Modificación de Fitness
En representacion_binaria.py, modifica la función calcular_fitness para:
Penalizar grupos con varianza alta de notas
Premiar diversidad (mezclar alumnos de diferentes rendimientos)
Compara los resultados con la versión original

### 🔷 Modificaciones:

## ✅ Actividad 3: Nuevo Operador Genético
En representacion_real.py, implementa un operador de mutación diferente:

def mutacion_gaussiana(cromosoma, sigma=0.1):
    # Tu implementación aquí
    # Debe mantener la normalización (suma = 1)
    
### 🔷 Prueba con diferentes valores de sigma:

## ✅ Actividad 4: Restricciones Adicionales
Modifica representacion_permutacional.py para agregar una restricción:
  Los alumnos con notas < 11 no pueden estar todos en el mismo examen
  Ajusta la función de fitness para penalizar soluciones que violen esta restricción

### 🔷 Modificaciones:


## ✅ Actividad 5: Visualización (Avanzado)
Crea un nuevo archivo visualizacion.py que:

### 🔷 Grafique la evolución del fitness por generación

### 🔷 Muestre un histograma de notas por examen

### 🔷 Compare las distribuciones de las 3 representaciones

## ✅ Actividad 6: Problema Extendido
Modifica uno de los programas para distribuir los alumnos en 4 exámenes

### 🔷 ¿Qué cambios necesitas hacer en el cromosoma?

### 🔷 ¿Cómo afecta esto a la convergencia del algoritmo?

