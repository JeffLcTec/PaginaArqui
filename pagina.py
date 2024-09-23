import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

# Configuración de página principal
st.set_page_config(page_title="Monitoreo de Temperatura y Humedad", layout="centered")

# Diseño de la página principal
st.markdown("<h1 style='text-align: center; color: white;'>Monitoreo de Temperatura y Humedad</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: gray;'>Bienvenido al portal de monitoreo en tiempo real</h3>", unsafe_allow_html=True)

# Imagen o ícono decorativo
st.image("TecLogo.png", use_column_width=True)

# Botón de ingreso
if st.button('Ver Datos'):
    st.write("Datos cargando...")

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

