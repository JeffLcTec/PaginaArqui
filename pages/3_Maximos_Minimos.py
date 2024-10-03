import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Cargar datos del archivo JSON
archivo = pd.read_json("temperatura.json")
datos = pd.json_normalize(archivo['datos'])

# Convertir las columnas a sus respectivos tipos
datos['dia'] = pd.to_datetime(datos['dia']).dt.date
datos['hora'] = pd.to_datetime(datos['hora'], format='%H:%M:%S').dt.time
datos['temperatura'] = pd.to_numeric(datos['temperatura'], errors='coerce')
datos['humedad'] = pd.to_numeric(datos['humedad'], errors='coerce')


# Crear opciones en el sidebar
st.sidebar.title("Opciones de Selección")
modo_seleccion = st.sidebar.radio("Selecciona cómo quieres ver los máximos y mínimos:", ("Por rango de días", "Por horas en un día"))

# Opción 1: Por rango de días
if modo_seleccion == "Por rango de días":
    st.write('# Máximos y mínimos por rango de días')
    col1,col2,col3 = st.columns([2, 3, 1]) 
    with col3:
      if st.button("Regresar"):
          st.switch_page("Inicio.py")
    # Cuadro de selección de Fecha de Inicio y Fin
    fecha_inicio = st.selectbox("Seleccionar Fecha de Inicio", datos['dia'].unique())
    
    fecha_inicio = pd.to_datetime(fecha_inicio).date()
    datos['dia'] = pd.to_datetime(datos['dia']).dt.date
    # Selección de fecha de fin solo con las fechas filtradas
    fechas_disponibles_fin = datos[datos['dia'] > fecha_inicio]['dia'].unique()
    
    # Selección de fecha de fin solo con las fechas filtradas
    fecha_fin = st.selectbox("Seleccionar Fecha de Fin", fechas_disponibles_fin)
    
    # Filtrar datos entre las fechas seleccionadas
    if pd.to_datetime(fecha_inicio) <= pd.to_datetime(fecha_fin):
        datos_filtrados = datos[(datos['dia'] >= fecha_inicio) & (datos['dia'] <= fecha_fin)]
        
        # Obtener los días con la temperatura y humedad máxima y mínima
        dia_max_temp = datos_filtrados.loc[datos_filtrados['temperatura'].idxmax()]
        dia_min_temp = datos_filtrados.loc[datos_filtrados['temperatura'].idxmin()]
        dia_max_humedad = datos_filtrados.loc[datos_filtrados['humedad'].idxmax()]
        dia_min_humedad = datos_filtrados.loc[datos_filtrados['humedad'].idxmin()]

        # Crear un DataFrame para mostrar estos datos
        resumen_rango = pd.DataFrame({
            'Día': [dia_max_temp['dia'], dia_min_temp['dia'], dia_max_humedad['dia'], dia_min_humedad['dia']],
            'Descripción': ['Temperatura Máxima', 'Temperatura Mínima', 'Humedad Máxima', 'Humedad Mínima'],
            'Valor': [dia_max_temp['temperatura'], dia_min_temp['temperatura'], dia_max_humedad['humedad'], dia_min_humedad['humedad']]
        })

        # Mostrar los datos en Streamlit
        st.write("Resumen de máximos y mínimos en el rango de días:")
        st.write(resumen_rango)
    else:
        st.error("La fecha de inicio debe ser anterior o igual a la fecha de fin.")

# Opción 2: Por horas en un día específico
elif modo_seleccion == "Por horas en un día":
    st.write('# Máximos y mínimos por horas en un día')
    col1,col2,col3 = st.columns([2, 3, 1]) 
    with col3:
      if st.button("Regresar"):
          st.switch_page("Inicio.py")
    # Selección de fecha
    fecha_seleccionada = st.selectbox("Seleccionar Día", datos['dia'].unique())

    # Filtrar datos para el día seleccionado
    datos_filtrados = datos[datos['dia'] == fecha_seleccionada]

    if not datos_filtrados.empty:
        # Obtener la hora con la temperatura y humedad máxima y mínima
        hora_max_temp = datos_filtrados.loc[datos_filtrados['temperatura'].idxmax()]
        hora_min_temp = datos_filtrados.loc[datos_filtrados['temperatura'].idxmin()]
        hora_max_humedad = datos_filtrados.loc[datos_filtrados['humedad'].idxmax()]
        hora_min_humedad = datos_filtrados.loc[datos_filtrados['humedad'].idxmin()]

        # Crear un DataFrame para mostrar estos datos
        resumen_horas = pd.DataFrame({
            'Hora': [hora_max_temp['hora'], hora_min_temp['hora'], hora_max_humedad['hora'], hora_min_humedad['hora']],
            'Descripción': ['Temperatura Máxima', 'Temperatura Mínima', 'Humedad Máxima', 'Humedad Mínima'],
            'Valor': [hora_max_temp['temperatura'], hora_min_temp['temperatura'], hora_max_humedad['humedad'], hora_min_humedad['humedad']]
        })

        # Mostrar los datos en Streamlit
        st.write("Resumen de máximos y mínimos por horas en el día:")
        st.write(resumen_horas)
    else:
        st.error("No se encontraron datos para el día seleccionado.")
