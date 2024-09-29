import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
import json

st.write('# Promedio por día')

# Cargar los datos desde el archivo JSON
archivo = pd.read_json("temperatura.json")
datos = pd.json_normalize(archivo['datos'])

# Convertir la columna 'dia' a datetime para poder filtrar
datos['dia'] = pd.to_datetime(datos['dia']).dt.date

# Convertir la columna 'hora' de cadena a tipo datetime en formato de tiempo
datos['hora'] = pd.to_datetime(datos['hora'], format='%H:%M:%S', errors='coerce')

# Convertir las columnas 'temperatura' y 'humedad' a valores numéricos
datos['temperatura'] = pd.to_numeric(datos['temperatura'], errors='coerce')
datos['humedad'] = pd.to_numeric(datos['humedad'], errors='coerce')

# Eliminar fechas duplicadas para el selector de fecha
datos_sin_duplicados = datos.drop_duplicates(subset=['dia'])

# Selección de fecha
fecha_seleccionada = st.selectbox("Seleccionar Fecha", datos_sin_duplicados['dia'].unique())

col1, col2, col3 = st.columns([2, 3, 1])
with col3:
    if st.button("Regresar"):
        st.switch_page("Inicio.py")

with col1:
    on = st.toggle("Ver Promedio")

if on:
    # Filtrar los datos según la fecha seleccionada
    datos_filtrados = datos[datos['dia'] == fecha_seleccionada]

    # Redondear las horas al inicio de cada hora
    datos_filtrados['hora'] = datos_filtrados['hora'].dt.floor('H')

    # Agrupar por la hora redondeada y calcular el promedio de temperatura y humedad
    datos_promediados = datos_filtrados.groupby('hora').agg({
        'temperatura': 'mean',
        'humedad': 'mean'
    }).reset_index()

    # Gráfico de temperatura
    fig_temp = go.Figure()
    fig_temp.add_trace(go.Scatter(x=datos_promediados['hora'], y=datos_promediados['temperatura'],
                                  mode='lines+markers', line=dict(color='red'), name='Temperatura'))
    fig_temp.update_layout(
        title=f"Temperatura Promedio de {fecha_seleccionada}",
        xaxis_title="Hora",
        yaxis_title="Temperatura (°C)",
        height=400
    )

    # Calcular el promedio general de temperatura
    promedio_temperatura = datos_promediados['temperatura'].mean()

    # Añadir la línea del promedio
    fig_temp.add_trace(go.Scatter(x=datos_promediados['hora'], y=[promedio_temperatura] * len(datos_promediados),
                                  mode='lines', line=dict(dash='dash', color='cyan'),
                                  name=f"Promedio General: {promedio_temperatura:.2f} °C"))

    # Gráfico de humedad
    fig_humedad = go.Figure()
    fig_humedad.add_trace(go.Scatter(x=datos_promediados['hora'], y=datos_promediados['humedad'],
                                     mode='lines+markers', line=dict(color='blue'), name='Humedad'))
    fig_humedad.update_layout(
        title=f"Humedad Promedio de {fecha_seleccionada}",
        xaxis_title="Hora",
        yaxis_title="Humedad (%)",
        height=400
    )

    # Calcular el promedio general de humedad
    promedio_humedad = datos_promediados['humedad'].mean()

    # Añadir la línea del promedio
    fig_humedad.add_trace(go.Scatter(x=datos_promediados['hora'], y=[promedio_humedad] * len(datos_promediados),
                                     mode='lines', line=dict(dash='dash', color='red'),
                                     name=f"Promedio General: {promedio_humedad:.2f} %"))

    # Mostrar los gráficos en Streamlit
    st.plotly_chart(fig_temp)
    st.plotly_chart(fig_humedad)

else:
    if fecha_seleccionada:
        try:
            # Filtrar los datos según la fecha seleccionada
            datos_filtrados = datos[datos['dia'] == fecha_seleccionada]

            # Redondear las horas al inicio de cada hora
            datos_filtrados['hora'] = pd.to_datetime(datos_filtrados['hora'], format='%H:%M:%S', errors='coerce').dt.floor('H')

            datos_promediados = datos_filtrados.groupby('hora').agg({
                  'temperatura': 'mean',
                  'humedad': 'mean'
               }).reset_index()
            
            # Gráfico de Temperatura
            fig_temp = go.Figure()
            fig_temp.add_trace(go.Scatter(x=datos_filtrados['hora'], y=datos_filtrados['temperatura'], mode='lines',
                                          name='Temperatura', line=dict(color='red')))
            fig_temp.update_layout(
                title=f"Temperatura de {fecha_seleccionada}",
                xaxis_title="Hora",
                yaxis_title="Temperatura (°C)",
                height=350
            )

            # Gráfico de Humedad
            fig_humedad = go.Figure()
            fig_humedad.add_trace(go.Scatter(x=datos_filtrados['hora'], y=datos_filtrados['humedad'], mode='lines',
                                             name='Humedad', line=dict(color='blue')))
            fig_humedad.update_layout(
                title=f"Humedad de {fecha_seleccionada}",
                xaxis_title="Hora",
                yaxis_title="Humedad (%)",
                height=350
            )

            # Mostrar los gráficos en Streamlit
            st.plotly_chart(fig_temp)
            st.plotly_chart(fig_humedad)
        except Exception as e:
            st.error(f"Error al procesar los datos: {e}")
