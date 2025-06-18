# SEMANA 7
Este dashboard interactivo se crea con Flask y Plotly para visualizar y analizar las notas de los estudiantes de un examen. A través de una interfaz web, el usuario puede ver diversos gráficos y estadísticas descriptivas relacionadas con el rendimiento de los estudiantes, tanto de manera general como por tipo de examen. Asi mismo se incluye la versión usando las librerias de matplot clásicas.

![Image](https://github.com/user-attachments/assets/b6307353-728e-4dac-91e2-ab49000cf0dd)


# SEMANA 8

## ✅ Actividad 1: Análisis Comparativo
Ejecuta los tres programas y compara los resultados  
Documenta tus observaciones en un archivo analisis.txt  

### 🔷 Resultados representación binaria

        REPRESENTACIÓN BINARIA
        Problema: Distribuir 39 alumnos en 3 exámenes (A, B, C) de forma equitativa
        Cromosoma: 117 bits (39 alumnos × 3 bits cada uno)
        Gen: [0,1,0] significa alumno asignado a examen B

        Generación 0: Mejor fitness = -0.0725
        Generación 20: Mejor fitness = -0.0363
        Generación 40: Mejor fitness = -0.0363
        Generación 60: Mejor fitness = -0.0363
        Generación 80: Mejor fitness = -0.0363

        Distribución final:
        Examen A: 13 alumnos, promedio = 15.46
        Alumnos: ['Alumno1', 'Alumno8', 'Alumno9', 'Alumno13', 'Alumno14']... (mostrando primeros 5)
        Examen B: 13 alumnos, promedio = 15.38
        Alumnos: ['Alumno2', 'Alumno3', 'Alumno5', 'Alumno7', 'Alumno11']... (mostrando primeros 5)
        Examen C: 13 alumnos, promedio = 15.38
        Alumnos: ['Alumno4', 'Alumno6', 'Alumno10', 'Alumno15', 'Alumno22']... (mostrando primeros 5)

        Verificación de equilibrio:
        Desviación estándar entre promedios: 0.0363

### 🔷 Resultados representación permutacional

        REPRESENTACIÓN PERMUTACIONAL
        Problema: Secuenciar alumnos para asignación ordenada a exámenes
        Cromosoma: Permutación de 39 índices de alumnos
        Decodificación: Posiciones [0-12] → Examen A, [13-25] → Examen B, [26-38] → Examen C

        Generación 0: Mejor fitness = 0.2637
        Generación 10: Mejor fitness = 0.2637
        Generación 20: Mejor fitness = 0.2637
        Generación 30: Mejor fitness = 0.2637
        Generación 40: Mejor fitness = 0.2637

        Asignación final por orden de secuencia:

        Examen A: 13 alumnos, promedio = 15.38
        Secuencia de alumnos:
            Posición 1: Alumno7 (Nota: 14.0)
            Posición 2: Alumno22 (Nota: 20.0)
            Posición 3: Alumno34 (Nota: 9.0)
            Posición 4: Alumno39 (Nota: 14.0)
            Posición 5: Alumno35 (Nota: 11.0)
            ... (mostrando primeros 5)

        Examen B: 13 alumnos, promedio = 15.46
        Secuencia de alumnos:
            Posición 1: Alumno13 (Nota: 14.0)
            Posición 2: Alumno10 (Nota: 17.0)
            Posición 3: Alumno33 (Nota: 18.0)
            Posición 4: Alumno18 (Nota: 16.0)
            Posición 5: Alumno19 (Nota: 20.0)
            ... (mostrando primeros 5)

        Examen C: 13 alumnos, promedio = 15.38
        Secuencia de alumnos:
            Posición 1: Alumno27 (Nota: 18.0)
            Posición 2: Alumno25 (Nota: 18.0)
            Posición 3: Alumno28 (Nota: 13.0)
            Posición 4: Alumno5 (Nota: 15.0)
            Posición 5: Alumno14 (Nota: 17.0)
            ... (mostrando primeros 5)

        Estadísticas finales:
        Promedios: A=15.38, B=15.46, C=15.38
        Rangos de notas: A=11, B=11, C=9
        Desviación estándar entre promedios: 0.0363

        Evolución del algoritmo:
        Fitness inicial: 0.2637
        Fitness final: 0.2637
        Mejora total: 0.0%

### 🔷 Resultados representación real

        REPRESENTACIÓN REAL
        Problema: Optimizar distribución de alumnos usando pesos probabilísticos
        Cromosoma: 117 valores reales (39 alumnos × 3 pesos normalizados)
        Gen: [0.2, 0.5, 0.3] representa probabilidades para exámenes A, B, C

        Generación 0: Mejor fitness = -1.1270
        Generación 30: Mejor fitness = -1.0911
        Generación 60: Mejor fitness = -1.0911
        Generación 90: Mejor fitness = -1.0911
        Generación 120: Mejor fitness = -1.0911

        Distribución optimizada:
        Examen A: 13 alumnos
        Promedio: 15.38, Varianza: 13.01
        Rango de notas: [9 - 20]
        Examen B: 13 alumnos
        Promedio: 15.38, Varianza: 10.70
        Rango de notas: [9 - 19]
        Examen C: 13 alumnos
        Promedio: 15.46, Varianza: 7.94
        Rango de notas: [11 - 20]

        Análisis de equilibrio:
        Promedios por examen: A=15.38, B=15.38, C=15.46
        Desviación estándar entre promedios: 0.0363
        Diferencia máxima entre promedios: 0.08

### 🔷 ¿Cuál representación logra mejor equilibrio entre los grupos?

**Análisis:**  
*Representación Binaria:* La desviación estándar entre los promedios de los tres exámenes es 0.0363, lo que indica una distribución bastante equilibrada de los alumnos entre los exámenes A, B y C.  
*Representación Permutacional:* La desviación estándar también es 0.0363, lo que sugiere que, aunque la secuenciación de los alumnos cambia, los promedios de las calificaciones entre los exámenes A, B y C siguen estando equilibrados de manera similar.  
*Representación Real:* La desviación estándar sigue siendo 0.0363 entre los promedios de los tres exámenes, lo que también muestra un buen equilibrio. La diferencia máxima entre los promedios es solo 0.08, lo que indica que los exámenes están muy bien equilibrados en cuanto a calificaciones.  

🔰 **Conclusión:**  
Las tres representaciones logran un equilibrio similar entre los grupos. No hay una representación que destaque significativamente sobre las otras en cuanto al equilibrio, ya que las desviaciones estándar entre los promedios son muy pequeñas en todos los casos. Sin embargo, todas las representaciones aseguran una distribución bastante equilibrada entre los tres exámenes.  
        
### 🔷 ¿Cuál converge más rápido? (observa las generaciones)

**Análisis:**  
*Representación Binaria:* En la Generación 0, el fitness es -0.0725, y mejora rápidamente a -0.0363 en la Generación 20, donde se estabiliza. El algoritmo converge rápidamente en las primeras 20 generaciones.  
*Representación Permutacional:* El fitness se mantiene constante desde la Generación 0 (con un valor de 0.2637) hasta la Generación 40, sin ninguna mejora. Esto indica que el algoritmo no converge ni mejora con el tiempo.  
*Representación Real:* El fitness mejora desde -1.1270 en la Generación 0 hasta -1.0911 en la Generación 30, y luego se estabiliza. La mejora ocurre principalmente en las primeras 30 generaciones.  

🔰 **Conclusión:**  
La representación binaria converge más rápido, con mejoras significativas en las primeras 20 generaciones, mientras que la representación real mejora de manera gradual y se estabiliza después de la Generación 30. La representación permutacional no muestra mejora en absoluto y no converge.  


## ✅ Actividad 2: Modificación de Fitness
En representacion_binaria.py, modifica la función calcular_fitness para:  
Penalizar grupos con varianza alta de notas  
Premiar diversidad (mezclar alumnos de diferentes rendimientos)  
Compara los resultados con la versión original  

### 🔷 Versión original

### 🔷 Modificación de fitness



## ✅ Actividad 3: Nuevo Operador Genético

En representacion_real.py, implementa un operador de mutación diferente:

        def mutacion_gaussiana(cromosoma, sigma=0.05):  # sigma controla la magnitud de la perturbación
            cromosoma_mutado = cromosoma.copy()  # Hacemos una copia del cromosoma para no modificar el original
            
            # Recorremos cada alumno (39 alumnos)
            for i in range(39):
                idx = i * 3  # Cada alumno tiene 3 valores correspondientes a sus asignaciones a los 3 exámenes
                genes = cromosoma_mutado[idx:idx+3]  # Extraemos los 3 valores correspondientes a ese alumno
                
                # Perturbamos cada peso con ruido gaussiano (normal) con media 0 y desviación estándar sigma
                genes_perturbados = [max(0.0, g + random.gauss(0, sigma)) for g in genes]
                # max(0.0, ...) asegura que los valores no sean negativos, ya que no puede haber asignaciones negativas
                
                suma = sum(genes_perturbados)  # Calculamos la suma de los valores perturbados
                if suma > 0:
                    # Normalizamos los valores para que sumen 1, ya que las asignaciones deben ser probabilidades
                    genes_normalizados = [g/suma for g in genes_perturbados]
                else:
                    # Si la suma es 0 (caso raro), asignamos valores iguales a cada examen
                    genes_normalizados = [1/3, 1/3, 1/3]
                
                # Reemplazamos los 3 valores originales con los valores normalizados
                cromosoma_mutado[idx:idx+3] = genes_normalizados
            
            return cromosoma_mutado  # Retornamos el cromosoma con las mutaciones gaussianas aplicadas


### 🔷 Representación real - Sigma 0.3
    
        Problema: Optimizar distribución de alumnos usando pesos probabilísticos
        Cromosoma: 117 valores reales (39 alumnos × 3 pesos normalizados)
        Generación 0: Mejor fitness = -1.0911
        Generación 30: Mejor fitness = -1.0911
        Generación 60: Mejor fitness = -1.0911
        Generación 90: Mejor fitness = -1.0911
        Generación 120: Mejor fitness = -1.0911
        
        Distribución optimizada:
        Examen A: 13 alumnos
          Promedio: 15.46, Varianza: 10.25
          Rango de notas: [9 - 20]
        Examen B: 13 alumnos
          Promedio: 15.38, Varianza: 11.01
          Rango de notas: [9 - 20]
        Examen C: 13 alumnos
          Promedio: 15.38, Varianza: 10.39
          Rango de notas: [10 - 20]
        
        Análisis de equilibrio:
        Promedios por examen: A=15.46, B=15.38, C=15.38
        Desviación estándar entre promedios: 0.0363
        Diferencia máxima entre promedios: 0.08
        
        
### 🔷 Representación real - Sigma 0.1

        Problema: Optimizar distribución de alumnos usando pesos probabilísticos
        Cromosoma: 117 valores reales (39 alumnos × 3 pesos normalizados)
        Generación 0: Mejor fitness = -1.0911
        Generación 30: Mejor fitness = -1.0911
        Generación 60: Mejor fitness = -1.0911
        Generación 90: Mejor fitness = -1.0911
        Generación 120: Mejor fitness = -1.0911
        
        Distribución optimizada:
        Examen A: 13 alumnos
          Promedio: 15.46, Varianza: 10.09
          Rango de notas: [10 - 20]       
        Examen B: 13 alumnos
          Promedio: 15.38, Varianza: 9.62 
          Rango de notas: [9 - 19]        
        Examen C: 13 alumnos
          Promedio: 15.38, Varianza: 11.93
          Rango de notas: [9 - 20]
        
        Análisis de equilibrio:
        Promedios por examen: A=15.46, B=15.38, C=15.38
        Desviación estándar entre promedios: 0.0363
        Diferencia máxima entre promedios: 0.08
        
        
### 🔷 Representación real - Sigma 0.05

        Problema: Optimizar distribución de alumnos usando pesos probabilísticos
        Cromosoma: 117 valores reales (39 alumnos × 3 pesos normalizados)       
        Generación 0: Mejor fitness = -1.0911
        Generación 30: Mejor fitness = -1.0911
        Generación 60: Mejor fitness = -1.0911
        Generación 90: Mejor fitness = -1.0911
        Generación 120: Mejor fitness = -1.0911
        
        Distribución optimizada:
        Examen A: 13 alumnos
          Promedio: 15.38, Varianza: 7.16
          Rango de notas: [10 - 19]      
        Examen B: 13 alumnos
          Promedio: 15.38, Varianza: 9.62
          Rango de notas: [9 - 20]
        Examen C: 13 alumnos
          Promedio: 15.46, Varianza: 14.86
          Rango de notas: [9 - 20]
        
        Análisis de equilibrio:
        Promedios por examen: A=15.38, B=15.38, C=15.46
        Desviación estándar entre promedios: 0.0363
        Diferencia máxima entre promedios: 0.08
    
### 🔷 Prueba con diferentes valores de sigma:
**🔰Sigma = 0.3:** Genera soluciones con notas más dispersas (mayor varianza) y fitness constante en todas las generaciones, sin mejoras significativas.  
**🔰Sigma = 0.1:** Soluciones más equilibradas, con promedios de notas similares y una varianza un poco menor que con sigma = 0.3, resultando en una mejor estabilidad.  
**🔰Sigma = 0.05:** Menor variabilidad en las notas, con una varianza más baja en el examen A y notas más consistentes.  

## ✅ Actividad 4: Restricciones Adicionales
Modifica representacion_permutacional.py para agregar una restricción:  
  Los alumnos con notas < 11 no pueden estar todos en el mismo examen  
  Ajusta la función de fitness para penalizar soluciones que violen esta restricción  

### 🔷 **Función `verificar_restriccion`**

Esta función verifica si la restricción de que "los alumnos con notas menores a 11 no pueden estar todos en el mismo examen" se cumple. Si se viola esta restricción, se devuelve una violación que se utilizará en el cálculo del fitness.  

    # Los alumnos con notas < 11 no pueden estar todos en el mismo examen
    def verificar_restriccion(asignaciones):
        violacion = 0  # Contador de violaciones de la restricción
        
        # Recorremos cada examen (A, B, C) para verificar la restricción
        for examen in ['A', 'B', 'C']:
            alumnos_examen = asignaciones[examen]  # Lista de alumnos asignados al examen
            notas_examen = [notas[i] for i in alumnos_examen]  # Notas de los alumnos en ese examen
            
            # Verificamos si todos los alumnos en el examen tienen notas < 11
            if len([nota for nota in notas_examen if nota < 11]) == len(notas_examen):
                violacion += 1  # Si todos los alumnos tienen notas < 11, incrementamos la violación
        
        return violacion  # Retornamos el número de violaciones de la restricción


### 🔷 **Modificación en la Función `calcular_fitness`**

    # Modificar la función de fitness para penalizar si la restricción es violada
    def calcular_fitness(cromosoma):
        asignaciones = decodificar_cromosoma(cromosoma)  # Decodificamos el cromosoma para obtener las asignaciones
        
        # Verificamos si la restricción fue violada y aplicamos una penalización
        penalizacion = verificar_restriccion(asignaciones) * 10  # Penalización de 10 por cada violación de la restricción
        
        promedios = {}  # Diccionario para almacenar los promedios de cada examen
        for examen in ['A', 'B', 'C']:  # Recorremos los 3 exámenes
            indices = asignaciones[examen]  # Alumnos asignados a este examen
            notas_examen = [notas[i] for i in indices]  # Notas de los alumnos asignados al examen
            promedios[examen] = np.mean(notas_examen)  # Calculamos el promedio de notas por examen
        
        # Calculamos la desviación estándar entre los promedios de los tres exámenes
        desv_promedios = np.std(list(promedios.values()))
        
        bonus_diversidad = 0  # Variable para agregar un bono por diversidad en la distribución
        for examen in ['A', 'B', 'C']:  # Comprobamos la diversidad en cada examen
            indices = asignaciones[examen]
            notas_examen = [notas[i] for i in indices]
            
            # Si la diferencia entre la nota más alta y la más baja es mayor que 5, agregamos un bono de diversidad
            if max(notas_examen) - min(notas_examen) > 5:
                bonus_diversidad += 0.1  # Añadimos 0.1 al bono de diversidad
        
        # El fitness final se calcula restando la desviación de los promedios, sumando el bono de diversidad y restando la penalización
        fitness = -desv_promedios + bonus_diversidad - penalizacion
        
        return fitness  # Retornamos el fitness final, que ahora incluye penalización y bono por diversidad


### 🔷 **Explicación de la Función mutacion**

    # Función de mutación: intercambiamos los exámenes de dos alumnos aleatorios
    def mutacion(cromosoma):
        cromosoma_mutado = cromosoma.copy()  # Creamos una copia del cromosoma para no modificar el original
        
        # Seleccionamos dos alumnos aleatorios para intercambiar sus asignaciones
        alumno1 = random.randint(0, 38)  # Alumno 1 (aleatorio)
        alumno2 = random.randint(0, 38)  # Alumno 2 (aleatorio)
        
        idx1 = alumno1 * 3  # Índice de inicio para el alumno 1 (cada alumno tiene 3 valores)
        idx2 = alumno2 * 3  # Índice de inicio para el alumno 2
        
        # Identificamos el examen asignado a cada alumno
        examen1 = [i for i in range(3) if cromosoma_mutado[idx1 + i] == 1][0]
        examen2 = [i for i in range(3) if cromosoma_mutado[idx2 + i] == 1][0]
        
        # Si los alumnos están asignados a exámenes diferentes, los intercambiamos
        if examen1 != examen2:
            cromosoma_mutado[idx1:idx1+3] = [0, 0, 0]  # Limpiamos la asignación original del alumno 1
            cromosoma_mutado[idx1 + examen2] = 1  # Asignamos el examen del alumno 2 al alumno 1
            
            cromosoma_mutado[idx2:idx2+3] = [0, 0, 0]  # Limpiamos la asignación original del alumno 2
            cromosoma_mutado[idx2 + examen1] = 1  # Asignamos el examen del alumno 1 al alumno 2
        
        return cromosoma_mutado  # Retornamos el cromosoma mutado


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
