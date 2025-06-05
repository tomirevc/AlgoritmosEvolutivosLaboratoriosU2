import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Cargar el archivo CSV de notas
file_path = 'notas_1u.csv'  # Cambia esta ruta a la ubicación de tu archivo CSV
data = pd.read_csv(file_path)

# Calcular estadísticas descriptivas básicas para las notas
estadisticas = data['Nota'].describe()

# Imprimir las estadísticas descriptivas de las notas
print("Estadísticas descriptivas de las notas:")
print(estadisticas)

# Estadísticas descriptivas por tipo de examen
print("\nEstadísticas descriptivas por Tipo de Examen:")
print(data.groupby('Tipo_Examen')['Nota'].describe())

# Visualización: Histograma y Boxplot de las notas en general
plt.figure(figsize=(14, 7))
plt.suptitle('Análisis Estadístico de las Notas de los Estudiantes', fontsize=18)

# Subgráfico 1: Histograma con KDE para todas las notas
plt.subplot(1, 2, 1)
sns.histplot(data['Nota'], kde=True, color='skyblue', bins=10, line_kws={'color': 'blue', 'lw': 2})
plt.title('Distribución de Notas', fontsize=16)
plt.xlabel('Nota', fontsize=12)
plt.ylabel('Frecuencia', fontsize=12)
plt.grid(True)

# Subgráfico 2: Boxplot general para todas las notas
plt.subplot(1, 2, 2)
sns.boxplot(x=data['Nota'], color='lightcoral')
plt.title('Distribución de Notas - Boxplot', fontsize=16)
plt.xlabel('Nota', fontsize=12)

# Añadir línea de la mediana y cuartiles
plt.axvline(estadisticas['50%'], color='red', linestyle='--', label=f'Mediana: {estadisticas["50%"]:.2f}')
plt.axvline(estadisticas['25%'], color='green', linestyle='--', label=f'Q1: {estadisticas["25%"]:.2f}')
plt.axvline(estadisticas['75%'], color='green', linestyle='--', label=f'Q3: {estadisticas["75%"]:.2f}')

# Mostrar leyenda y mejorar la visualización
plt.legend()
plt.grid(True)

# Aumentar el número de ticks en el eje X y Y
plt.subplot(1, 2, 1)  # Histograma
plt.gca().xaxis.set_major_locator(plt.MaxNLocator(integer=True, prune='lower', nbins=15))  # Ajusta el número de ticks en el eje X
plt.gca().yaxis.set_major_locator(plt.MaxNLocator(nbins=10))  # Ajusta el número de ticks en el eje Y

plt.subplot(1, 2, 2)  # Boxplot
plt.gca().xaxis.set_major_locator(plt.MaxNLocator(integer=True, prune='lower', nbins=15))  # Ajusta el número de ticks en el eje X

# Ajustar el layout y mostrar los gráficos
plt.tight_layout()

# Visualización: Análisis por Tipo de Examen
# Crear gráficos de distribución por tipo de examen
plt.figure(figsize=(14, 7))
plt.suptitle('Distribución de Notas por Tipo de Examen', fontsize=18)

# Subgráfico 1: Histograma por Tipo de Examen
plt.subplot(1, 2, 1)
sns.histplot(data=data, x='Nota', hue='Tipo_Examen', kde=True, multiple='stack', palette='Set2', bins=10)
plt.title('Histograma por Tipo de Examen', fontsize=16)
plt.xlabel('Nota', fontsize=12)
plt.ylabel('Frecuencia', fontsize=12)
plt.grid(True)

# Subgráfico 2: Boxplot por Tipo de Examen
plt.subplot(1, 2, 2)
sns.boxplot(x='Tipo_Examen', y='Nota', data=data, palette='Set2')
plt.title('Distribución de Notas por Tipo de Examen - Boxplot', fontsize=16)
plt.xlabel('Tipo de Examen', fontsize=12)
plt.ylabel('Nota', fontsize=12)

# Ajustar el layout y mostrar los gráficos
plt.tight_layout()
plt.show()
