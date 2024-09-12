import streamlit as st
import plotly.express as px
import pandas as pd

# Datos de ejemplo para el gráfico
data = pd.DataFrame({
    'x': range(10),
    'y': [i**2 for i in range(10)]
})

# Crear un gráfico con Plotly
fig = px.line(data, x='x', y='y', title="Gráfico Fijo")

# Configuración de la página en Streamlit
st.set_page_config(layout="wide")

# CSS para fijar el gráfico en la columna derecha
st.markdown("""
    <style>
    .fixed-content {
        position: -webkit-sticky;
        position: sticky;
        top: 0;
        height: 100vh;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .scrollable-text {
        height: 100vh;
        overflow-y: scroll;
    }
    </style>
    """, unsafe_allow_html=True)

# Crear las dos columnas
col1, col2 = st.columns([1, 2])

# Columna 1: Texto desplazable
with col1:
    st.markdown('<div class="scrollable-text">', unsafe_allow_html=True)
    st.header("Sección 1")
    st.write("Este texto se desplaza mientras el gráfico permanece fijo. Aquí puedes poner historias de datos o explicaciones adicionales.")
    st.write("Texto adicional para hacer la sección más larga y asegurar que se puede hacer scroll. " * 20)

    st.header("Sección 2")
    st.write("Continúa con más información y el gráfico sigue siendo fijo en la otra columna.")
    st.write("Texto adicional para hacer la sección más larga y asegurar que se puede hacer scroll. " * 20)

    st.header("Sección 3")
    st.write("Finalmente, esta es la sección final.")
    st.write("Texto adicional para hacer la sección más larga y asegurar que se puede hacer scroll. " * 20)
    st.markdown('</div>', unsafe_allow_html=True)

# Columna 2: Gráfico fijo
with col2:
    st.markdown('<div class="fixed-content">', unsafe_allow_html=True)
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
