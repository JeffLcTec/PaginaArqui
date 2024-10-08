import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
import json
st.write('# Promedio por rango días')
archivo = pd.read_json("temperatura.json")
datos = pd.json_normalize(archivo['datos'])
fechas_df = datos[['dia']]
   
# Convertir las columnas de temperatura y humedad a tipo float
datos['temperatura'] = pd.to_numeric(datos['temperatura'], errors='coerce')
datos['humedad'] = pd.to_numeric(datos['humedad'], errors='coerce')   
   
# Cuadro de selección para Fecha de Inicio y Fin
fecha_inicio = st.selectbox("Fecha de inicio", datos['dia'].unique())

fecha_inicio = pd.to_datetime(fecha_inicio).date()
datos['dia'] = pd.to_datetime(datos['dia']).dt.date
# Selección de fecha de fin solo con las fechas filtradas
fechas_disponibles_fin = datos[datos['dia'] > fecha_inicio]['dia'].unique()

# Selección de fecha de fin solo con las fechas filtradas
fecha_fin = st.selectbox("Fecha final", fechas_disponibles_fin)

col1,col2,col3 = st.columns([2, 3, 1]) 
with col3:
   if st.button("Regresar"):
      st.switch_page("Inicio.py")
   
with col1:
   on = st.toggle("Ver promedio")

if on:

    # Convertir las fechas seleccionadas a formato datetime
   fecha_inicio = pd.to_datetime(fecha_inicio).date()
   fecha_fin = pd.to_datetime(fecha_fin).date()
    
    
    # Convertir la columna 'dia' a datetime para poder filtrar
   datos['dia'] = pd.to_datetime(datos['dia']).dt.date
    
    # Convertir a tipo float
   datos['temperatura'] = datos['temperatura'].astype(float)
   datos['humedad'] = datos['humedad'].astype(float)
    
    # Filtrar los datos según el rango de fechas
   datos_filtrados = datos[(datos['dia'] >= fecha_inicio) & (datos['dia'] <= fecha_fin)]
   # Agrupar por 'dia' y calcular el promedio de temperatura y humedad
 
   datos_filtrados = datos_filtrados.groupby('dia').agg({
      'temperatura': 'mean',
      'humedad': 'mean'
   }).reset_index()

   # Redondear los promedios a 2 decimales directamente
   datos_filtrados['temperatura'] = datos_filtrados['temperatura'].round(2)
   datos_filtrados['humedad'] = datos_filtrados['humedad'].round(2)
   
    # Calcular el promedio de temperatura en el rango de fechas
   promedio_temperatura = datos_filtrados['temperatura'].mean()
   promedio_humedad = datos_filtrados['humedad'].mean()
    # Crear la figura del gráfico
   fig = go.Figure()
   fig1 = go.Figure() 
    # Añadir la línea de temperaturas
   fig.add_trace(go.Scatter(x=datos_filtrados['dia'], y=datos_filtrados['temperatura'],mode='lines+markers', line=dict(color='red'),name='Temperatura'))
   fig.update_layout(
            title=f"Temperatura Promedio desde {fecha_inicio} hasta {fecha_fin}",
            xaxis_title="Fecha",
            yaxis_title="Temperatura (°C)",
            height=400,
            xaxis_tickformat='%Y-%m-%d',
            xaxis=dict(tickmode='array', tickvals=datos_filtrados['dia'])
         ) 
    # Añadir la línea del promedio
   fig.add_trace(go.Scatter(x=datos_filtrados['dia'], y=[promedio_temperatura] * len(datos_filtrados),
                           mode='lines', line=dict(dash='dash', color='cyan'),
                           name=f"Promedio: {promedio_temperatura:.2f} °C"))
    
    # Añadir título y etiquetas
   fig.update_layout(
      title=f"Temperatura desde {fecha_inicio} hasta {fecha_fin}",
      xaxis_title="Fecha",
      yaxis_title="Temperatura (°C)"
   )
   
   fig1.add_trace(go.Scatter(x=datos_filtrados['dia'], y=datos_filtrados['humedad'],mode='lines+markers',line=dict(color='blue'), name='Humedad'))
   fig1.update_layout(
            title=f"Humedad Promedio desde {fecha_inicio} hasta {fecha_fin}",
            xaxis_title="Fecha",
            yaxis_title="Humedad (%)",
            height=400,
            xaxis_tickformat='%Y-%m-%d',
            xaxis=dict(tickmode='array', tickvals=datos_filtrados['dia'])
         ) 
    # Añadir la línea del promedio
   fig1.add_trace(go.Scatter(x=datos_filtrados['dia'], y=[promedio_humedad] * len(datos_filtrados),
                           mode='lines', line=dict(dash='dash', color='Red'),
                           name=f"Promedio: {promedio_humedad:.2f} %"))
    
    # Añadir título y etiquetas
   fig1.update_layout(
      title=f"Humedad promedio desde {fecha_inicio} hasta {fecha_fin}",
      xaxis_title="Fecha",
      yaxis_title="Humedad %"
   )
    # Mostrar el gráfico en Streamlit
   st.plotly_chart(fig)
   st.plotly_chart(fig1)
else:
   if fecha_inicio and fecha_fin:
      try:
         fecha_inicio = pd.to_datetime(fecha_inicio).date()
         fecha_fin = pd.to_datetime(fecha_fin).date()
           
         
           # Convertir la columna 'dia' a datetime para poder filtrar
         datos['dia'] = pd.to_datetime(datos['dia']).dt.date
         
         datos['temperatura'] = datos['temperatura'].astype(float)   
         
         datos_filtrados = datos[(datos['dia'] >= fecha_inicio) & (datos['dia'] <= fecha_fin)]
         # Agrupar por 'dia' y calcular el promedio de temperatura y humedad
         datos_filtrados = datos_filtrados.groupby('dia').agg({
            'temperatura': 'mean',
            'humedad': 'mean'
         }).reset_index()

         datos_filtrados['temperatura'] = datos_filtrados['temperatura'].round(2)
         datos_filtrados['humedad'] = datos_filtrados['humedad'].round(2)

         # Gráfico de Temperatura
         fig_temp = go.Figure()
         fig_temp.add_trace(go.Scatter(x=datos_filtrados['dia'], y=datos_filtrados['temperatura'], mode='lines', name='Temperatura', line=dict(color='red')))
         fig_temp.update_layout(
               title=f"Temperatura desde {fecha_inicio} hasta {fecha_fin}",
               xaxis_title="Fecha",
               yaxis_title="Temperatura (°C)",
               height=350,
               xaxis_tickformat='%Y-%m-%d',
               xaxis=dict(tickmode='array', tickvals=datos_filtrados['dia'])
         )
      
            # Gráfico de Humedad
         fig_humedad = go.Figure()
         fig_humedad.add_trace(go.Scatter(x=datos_filtrados['dia'], y=datos_filtrados['humedad'], mode='lines', name='Humedad', line=dict(color='blue')))
         fig_humedad.update_layout(
               title=f"Humedad desde {fecha_inicio} hasta {fecha_fin}",
               xaxis_title="Fecha",
               yaxis_title="Humedad (%)",
               height=350,
               xaxis_tickformat='%Y-%m-%d',
               xaxis=dict(tickmode='array', tickvals=datos_filtrados['dia'])
         )
      
            # Mostrar los gráficos en Streamlit
         st.plotly_chart(fig_temp)
         st.plotly_chart(fig_humedad)
      except Exception as e:
         st.error(f"Error al procesar el rango de fechas: {e}")
