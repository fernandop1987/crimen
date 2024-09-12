import streamlit as st
import plotly.express as px
import pandas as pd

# Configuración de la página completa y título
st.set_page_config(layout="wide", page_title="Mi Historia de Datos")

# Agregar CSS personalizado para el estilo
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
    }
    .big-title {
        font-size:40px !important;
        font-family: 'Helvetica', sans-serif;
        color: #333333;
    }
    .custom-header {
        font-size: 25px;
        color: #FF6347;
        text-align: center;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# Título grande y centrado
st.markdown('<p class="big-title">Historias de Datos Interactivas</p>', unsafe_allow_html=True)

# Incluir una imagen de fondo
st.image("background_image.jpg", use_column_width=True)



# Dividir la página en dos columnas
col1, col2 = st.columns(2)

# Datos de ejemplo y gráfico en la primera columna
data = {
    "Productos": ["Papa", "Tomate", "Zanahoria", "Lechuga"],
    "Precios": [1.50, 2.30, 1.80, 0.80]
}
df = pd.DataFrame(data)

with col1:
    st.subheader("Evolución de Precios")
    fig = px.bar(df, x="Productos", y="Precios", title="Precios de Productos")
    st.plotly_chart(fig, use_container_width=True)

# Texto y otro contenido en la segunda columna
with col2:
    st.markdown('<p class="custom-header">Análisis del precio de productos</p>', unsafe_allow_html=True)
    st.write("""
    En esta sección, mostramos la evolución de los precios de algunos productos clave 
    a lo largo del tiempo. Los datos se obtuvieron de informes semanales y 
    se visualizan de forma interactiva utilizando gráficos de barras.
    """)

import streamlit as st

st.title("Ejemplo de Scrollytelling")




# Footer o información adicional
st.markdown("---")
st.write("Creado por ABCData. Todos los derechos reservados.")
