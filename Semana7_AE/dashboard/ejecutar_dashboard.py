from flask import Flask, render_template
import pandas as pd
import webbrowser
import plotly.express as px
import plotly.graph_objects as go

# Crear la aplicación Flask
app = Flask(__name__)

# Leer el archivo CSV de notas
file_path = 'notas_1u.csv'
data = pd.read_csv(file_path)

# Calcular estadísticas descriptivas
estadisticas = data['Nota'].describe()

# Calcular estadísticas por Tipo de Examen
estadisticas_por_tipo = data.groupby('Tipo_Examen')['Nota'].describe()

# Crear gráficos con Plotly
# Histograma de las notas
fig_hist = px.histogram(data, x='Nota', nbins=10, title="Distribución de Notas")

# Boxplot de las notas
fig_box = px.box(data, x='Tipo_Examen', y='Nota', title="Distribución de Notas por Tipo de Examen")

# Histograma apilado por Tipo de Examen
fig_hist_tipo = px.histogram(data, x='Nota', color='Tipo_Examen', nbins=10, title="Histograma por Tipo de Examen", barmode='stack')

# Gráfico de barras de estadísticas descriptivas
fig_stats = go.Figure([
    go.Bar(
        x=['Examen A', 'Examen B', 'Examen C'],  # Tipos de Examen en el eje X
        y=[
            estadisticas_por_tipo.loc['A', 'mean'],  # Media de Examen A
            estadisticas_por_tipo.loc['B', 'mean'],  # Media de Examen B
            estadisticas_por_tipo.loc['C', 'mean']   # Media de Examen C
        ],  # Medias en el eje Y
        name='Promedio de Notas'  # Nombre de la serie
    )
])

fig_stats.update_layout(
    title='Comparación de Promedios por Tipo de Examen',
    xaxis_title='Tipo de Examen',
    yaxis_title='Promedio de Notas',
    showlegend=False  # No mostrar leyenda
)




# Ruta principal
@app.route('/')
def index():
    # Renderizar la plantilla y pasar los gráficos
    return render_template(
        'index.html',
        fig_hist=fig_hist.to_html(full_html=False),
        fig_box=fig_box.to_html(full_html=False),
        fig_hist_tipo=fig_hist_tipo.to_html(full_html=False),
        fig_stats=fig_stats.to_html(full_html=False),
        estadisticas=estadisticas.to_dict(),
        estadisticas_por_tipo=estadisticas_por_tipo.to_html()
    )


# Iniciar el servidor
if __name__ == "__main__":
    webbrowser.open("http://127.0.0.1:5000/")  # URL por defecto de Flask
    app.run(debug=True)
