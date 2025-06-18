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

![Image](https://github.com/user-attachments/assets/25b0dc99-40e4-41de-b4b2-b1f47014df2d)

🔰 **Binaria (Azul):** El fitness oscila mucho, indicando que el algoritmo explora el espacio de soluciones pero no converge rápidamente.
🔰 **Permutacional (Verde):** El fitness es más estable, lo que sugiere una optimización más controlada.
🔰 **Real (Rojo):** El fitness mejora constantemente, indicando que la representación real tiene una convergencia más eficiente hacia una solución óptima.

### 🔷 Muestre un histograma de notas por examen

![Image](https://github.com/user-attachments/assets/4444cca4-95b1-46ed-91f4-8436d140caac)

🔰 **Examen A (Azul):** La mayoría de los alumnos tienen notas altas.
🔰 **Examen B (Naranja):** Distribución más uniforme, con concentración en notas intermedias.
🔰 **Examen C (Verde):** Similar a los otros exámenes, con una ligera concentración en notas altas.

### 🔷 Compare las distribuciones de las 3 representaciones

![Image](https://github.com/user-attachments/assets/a727d1b6-6619-4abb-929c-380daf780703)

🔰 **Distribución Binaria:** En la representación binaria, hay una gran concentración de alumnos en un solo examen (A) y pocas variaciones entre los otros exámenes, lo que sugiere que el algoritmo binario puede tener dificultades para distribuir equitativamente a los alumnos.
🔰 **Distribución Permutacional:** En la representación permutacional, la distribución de las notas es más equilibrada, aunque aún se pueden notar algunas concentraciones en los exámenes A y C. Esta distribución es probablemente más eficiente que la binaria en cuanto a equidad.
🔰 **Distribución Real:** Similar a la permutacional, pero con una mejor distribución de los alumnos entre los exámenes, lo que sugiere que la representación real podría estar optimizando mejor la asignación de alumnos.

## ✅ Actividad 6: Problema Extendido
Modifica uno de los programas para distribuir los alumnos en 4 exámenes

### 🔷 ¿Qué cambios necesitas hacer en el cromosoma?

Anteriormente, el cromosoma tenía 3 bits por alumno, uno para cada examen (A, B, C).
Ahora, cada alumno tiene 4 bits para representar su asignación a uno de los 4 
exámenes (A, B, C, D). Esto hace que el cromosoma tenga un total de 156 bits (39 alumnos × 4 bits cada uno).

### 🔷 ¿Cómo afecta esto a la convergencia del algoritmo?

Al agregar un examen adicional, el espacio de búsqueda aumenta. Hay más combinaciones posibles 
de asignación para los alumnos, lo que hace que el algoritmo necesite más generaciones para 
converger a una solución óptima.
