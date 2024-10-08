import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

# Configuración de página principal
col1,col2, col3 = st.columns([1, 2, 1])  # Columnas con proporciones 1:2:1
with col2:
    st.image("TecLogo.png", width=250) 


st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@900&display=swap');

    .titulo {
        font-family: 'Montserrat', sans-serif;
        font-size: 48px;
        font-weight: 900;  /* Fuente gruesa */
        text-align: center;
        color: "white";
    }
    </style>
    <div class="titulo">
        Monitoreo de temperatura y humedad
    </div>
    """, 
    unsafe_allow_html=True
)
st.markdown("<h3 style='text-align: center; color: gray;'>Bienvenido al portal de monitoreo en tiempo real</h3>", unsafe_allow_html=True)

# Añadir un espaciado antes de las columnas
st.markdown("<br><br><br>", unsafe_allow_html=True)  # Añadir saltos de línea

col1, col2, col3 = st.columns([2, 2, 2])


# Botón de ingreso
with col1:
    if st.button('Ver Promedio-Dias'):
        st.switch_page("pages/1_Rango_Dia.py")
with col3:
    if st.button('Ver Promedio-Horas'):
        st.switch_page("pages/2_Promedio_Hora.py")
with col2:
    if st.button('Ver Maximos y Minimos'):
        st.switch_page("pages/3_Maximos_Minimos.py")
# Estilo CSS personalizado para darle un toque adicional
st.markdown("""
    <style>
    body {
        background-color: #1a1a1a;
        color: white;
    }
    h1, h3 {
        font-family: 'Arial', sans-serif;
    }
    </style>
    """, unsafe_allow_html=True)

<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Créditos</title>
  <link rel="stylesheet" href="styles.css"> <!-- Incluye los estilos de tu página -->
</head>
<body>
  <header>
    <h1>Créditos</h1>
  </header>
  <section>
    <h2>Equipo de Desarrollo</h2>
    <ul>
      <li><strong>Nombre Completo 1</strong> – Desarrollador Frontend</li>
      <li><strong>Nombre Completo 2</strong> – Desarrollador Backend</li>
      <li><strong>Nombre Completo 3</strong> – Diseñador UI/UX</li>
      <li><strong>Nombre Completo 4</strong> – Gestión de Proyectos</li>
      <li><strong>Nombre Completo 5</strong> – Desarrollador Full Stack</li>
    </ul>
  </section>
  <section>
    <h2>Colaboradores Especiales</h2>
    <ul>
      <li><strong>Nombre Completo 6</strong> – Consultor de Seguridad</li>
      <li><strong>Nombre Completo 7</strong> – Pruebas y Calidad</li>
    </ul>
  </section>
  <footer>
    <p>&copy; 2024 Nombre del Proyecto</p>
  </footer>
</body>
</html>
