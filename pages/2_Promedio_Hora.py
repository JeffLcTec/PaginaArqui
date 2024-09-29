import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
import json
st.write('# Promedio por dia')
archivo = pd.read_json("temperatura.json")
datos = pd.json_normalize(archivo['datos'])
fechas_df = datos[['dia']]
   
   
# Eliminar fechas duplicadas
datos_sin_duplicados = datos.drop_duplicates(subset=['dia'])

# Mostrar el DataFrame sin fechas duplicadas

   # Cuadro de selección para Fecha de Inicio
fecha_seleccionada = st.selectbox("Seleccionar Fecha ", datos_sin_duplicados[['dia']])
   
   # Cuadro de selección para Fecha de Fin


col1,col2,col3 = st.columns([2, 3, 1]) 
with col3:
   if st.button("Regresar"):
      st.switch_page("Inicio.py")
   
with col1:
   on = st.toggle("Ver Promedio")

if on:

   # Convertir las fechas seleccionadas a formato datetime
   fecha_seleccionada = pd.to_datetime(fecha_seleccionada).date()
 
    # Convertir la columna 'dia' a datetime para poder filtrar
   datos['dia'] = pd.to_datetime(datos['dia']).dt.date
   datos['hora'] = pd.to_datetime(datos['hora'], format='%H:%M:%S').dt.time
    # Convertir a tipo float
   datos['temperatura'] = pd.to_numeric(datos['temperatura'], errors='coerce')
   datos['humedad'] = pd.to_numeric(datos['humedad'], errors='coerce')
   
    # Filtrar los datos según el rango de fechas
   datos_filtrados = datos[(datos['dia'] == fecha_seleccionada)]
   datos_filtrados['hora'] = datos_filtrados['hora'].dt.floor('H')

    # Agrupar por hora para unificar los datos de la misma hora
   datos_filtrados = datos_filtrados.groupby('hora').agg({
        'temperatura': 'mean',
        'humedad': 'mean'
    }).reset_index()

    # Calcular el promedio de temperatura en el rango de fechas
   promedio_temperatura = datos_filtrados['temperatura'].mean()
   promedio_humedad = datos_filtrados['humedad'].mean()
    # Crear la figura del gráfico
   fig = go.Figure()
   fig1 = go.Figure() 
    # Añadir la línea de temperaturas
   fig.add_trace(go.Scatter(x=datos_filtrados['hora'], y=datos_filtrados['temperatura'],mode='lines+markers', line=dict(color='red'),name='Temperatura'))
   fig.update_layout(
            title=f"Temperatura Promedio de {fecha_seleccionada}",
            xaxis_title="Fecha",
            yaxis_title="Temperatura (°C)",
            height=400,
            xaxis_tickformat='%Y-%m-%d',
            xaxis=dict(tickmode='array', tickvals=datos_filtrados['hora'])
         ) 
    # Añadir la línea del promedio
   fig.add_trace(go.Scatter(x=datos_filtrados['hora'], y=[promedio_temperatura] * len(datos_filtrados),
                           mode='lines', line=dict(dash='dash', color='cyan'),
                           name=f"Promedio: {promedio_temperatura:.2f} °C"))
    
   
   fig1.add_trace(go.Scatter(x=datos_filtrados['hora'], y=datos_filtrados['humedad'],mode='lines+markers',line=dict(color='blue'), name='Humedad'))
   fig1.update_layout(
            title=f"Humedad Promedio de {fecha_seleccionada} ",
            xaxis_title="Fecha",
            yaxis_title="Humedad (%)",
            height=400,
            xaxis_tickformat='%Y-%m-%d',
            xaxis=dict(tickmode='array', tickvals=datos_filtrados['hora'])
         ) 
    # Añadir la línea del promedio
   fig1.add_trace(go.Scatter(x=datos_filtrados['hora'], y=[promedio_humedad] * len(datos_filtrados),
                           mode='lines', line=dict(dash='dash', color='Red'),
                           name=f"Promedio: {promedio_humedad:.2f} %"))
    
    # Añadir título y etiquetas
   fig1.update_layout(
      title=f"Humedad promedio de {fecha_seleccionada}",
      xaxis_title="Fecha",
      yaxis_title="Humedad %"
   )
    # Mostrar el gráfico en Streamlit
   st.plotly_chart(fig)
   st.plotly_chart(fig1)
else:
   if fecha_seleccionada :
       try:
         
         fecha_seleccionada = pd.to_datetime(fecha_seleccionada).date()
            
         
            # Convertir la columna 'dia' a datetime para poder filtrar
         datos['dia'] = pd.to_datetime(datos['dia']).dt.date
         datos['hora'] = pd.to_datetime(datos['hora'], format='%H:%M:%S', errors='coerce')
         datos['hora'] = datos['hora'].dt.strftime('%H:00')

               #Convertir las columnas 'temperatura' y 'humedad' a valores numéricos
         datos['temperatura'] = pd.to_numeric(datos['temperatura'], errors='coerce')
         datos['humedad'] = pd.to_numeric(datos['humedad'], errors='coerce')
         
         datos_filtrados = datos[(datos['dia'] == fecha_seleccionada)]
         

         # Agrupar por hora para unificar los datos de la misma hora
         datos_filtrados = datos_filtrados.groupby('hora').agg({
            'temperatura': 'mean',
            'humedad': 'mean'
         }).reset_index()
         promedio_temperatura = datos_filtrados['temperatura'].mean() 
           
            # Gráfico de Temperatura
         fig_temp = go.Figure()
         fig_temp.add_trace(go.Scatter(x=datos_filtrados['hora'], y=datos_filtrados['temperatura'], mode='lines', name='Temperatura', line=dict(color='red')))
         fig_temp.update_layout(
             title=f"Temperatura de {fecha_seleccionada}",
             xaxis_title="Fecha",
             yaxis_title="Temperatura (°C)",
             height=350,
             xaxis_tickformat='%Y-%m-%d',
             xaxis=dict(tickmode='array', tickvals=datos_filtrados['hora'])
         )
   
            # Gráfico de Humedad
         fig_humedad = go.Figure()
         fig_humedad.add_trace(go.Scatter(x=datos_filtrados['hora'], y=datos_filtrados['humedad'], mode='lines', name='Humedad', line=dict(color='blue')))
         fig_humedad.update_layout(
             title=f"Humedad de {fecha_seleccionada}",
             xaxis_title="Fecha",
             yaxis_title="Humedad (%)",
             height=350,
             xaxis_tickformat='%Y-%m-%d',
             xaxis=dict(tickmode='array', tickvals=datos_filtrados['hora'])
         )
   
            # Mostrar los gráficos en Streamlit
         st.plotly_chart(fig_temp)
         st.plotly_chart(fig_humedad)
       except Exception as e:
         st.error(f"Error al procesar el rango de fechas: {e}")
