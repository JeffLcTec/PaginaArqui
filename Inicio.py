import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

# Configuración de página principal
col1, col2, col3 = st.columns([1, 2, 1])  # Columnas con proporciones 1:2:1
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
        Monitoreo de Temperatura y Humedad
    </div>
    """, 
    unsafe_allow_html=True
)
st.markdown("<h3 style='text-align: center; color: gray;'>Bienvenido al portal de monitoreo en tiempo real</h3>", unsafe_allow_html=True)

# Imagen o ícono decorativo

# Botón de ingreso
if st.button('Ver Datos'):
    st.write("Datos cargando...")
    st.page_link(1_Rango_Dia.py)

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

