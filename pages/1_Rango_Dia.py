import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
st.write('# Promedio por Rango Dias')
archivo = pd.read_json("temperatura.json")
datos = pd.json_normalize(archivo['datos_ultimos_7_dias'])
fechas_df = datos[['dia']]
   
   
   
   # Cuadro de selección para Fecha de Inicio
fecha_inicio = st.selectbox("Seleccionar Fecha de Inicio", fechas_df)
   
   # Cuadro de selección para Fecha de Fin
fecha_fin = st.selectbox("Seleccionar Fecha de Fin", fechas_df)
   
on = st.toggle("Ver Promedio")

if on:
    st.write("Jue que pichudo mae") 
   # Crear el gráfico de las temperaturas en el tiempo
   fecha_inicio = pd.to_datetime(fecha_inicio).date()
   fecha_fin = pd.to_datetime(fecha_fin).date()
              
   st.write(f"Rango de fechas: {fecha_inicio} - {fecha_fin}")
      
           
              # Convertir la columna 'dia' a datetime para poder filtrar
   datos['dia'] = pd.to_datetime(datos['dia']).dt.date
          
   datos['temperatura'] = datos['temperatura'].astype(float)   
          
   datos_filtrados = datos[(datos['dia'] >= fecha_inicio) & (datos['dia'] <= fecha_fin)]
          
   promedio_temperatura = datos_filtrados['temperatura'].mean() 
   fig = go.Figure()
   
   # Añadir la línea de temperaturas
   fig.add_trace(go.Scatter(x=datos_filtrados['dia'], y=datos_filtrados['temperatura'],
                            mode='lines+markers', name='Temperatura'))
   
   # Añadir la línea de promedio
   fig.add_trace(go.Scatter(x=datos_filtrados['dia'], y=[promedio_temperatura] * len(datos_filtrados),
                            mode='lines', line=dict(dash='dash', color='red'),
                            name=f"Promedio: {promedio_temperatura:.2f} °C"))
   
   # Añadir título y etiquetas
   fig.update_layout(
       title=f"Temperatura desde {fecha_inicio} hasta {fecha_fin}",
       xaxis_title="Fecha",
       yaxis_title="Temperatura (°C)"
   )
   
   # Mostrar el gráfico en Streamlit o como gráfico interactivo
   fig.show()
else:
   if fecha_inicio and fecha_fin:
       try:
           # Dividir la cadena en dos partes (antes y después del guion '-')
          
              
           fecha_inicio = pd.to_datetime(fecha_inicio).date()
           fecha_fin = pd.to_datetime(fecha_fin).date()
              
           st.write(f"Rango de fechas: {fecha_inicio} - {fecha_fin}")
      
           
              # Convertir la columna 'dia' a datetime para poder filtrar
           datos['dia'] = pd.to_datetime(datos['dia']).dt.date
          
           datos['temperatura'] = datos['temperatura'].astype(float)   
          
           datos_filtrados = datos[(datos['dia'] >= fecha_inicio) & (datos['dia'] <= fecha_fin)]
          
           promedio_temperatura = datos_filtrados['temperatura'].mean() 
             
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
