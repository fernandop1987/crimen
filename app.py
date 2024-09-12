import streamlit as st
import plotly.express as px
import pandas as pd

# Simulamos algunos datos para el gráfico
data = pd.DataFrame({
    'x': range(10),
    'y': [i**2 for i in range(10)]
})

# Creamos un gráfico básico con Plotly
fig = px.line(data, x='x', y='y', title="Gráfico Fijo")

# Configuración del layout de la página
st.set_page_config(layout="wide")

# CSS para hacer que el gráfico en la primera columna sea fijo
st.markdown("""
    <style>
    .fixed-content {
        position: sticky;
        top: 0;
        height: 100vh;
    }
    </style>
    """, unsafe_allow_html=True)

# Creamos una fila con dos columnas
col1, col2 = st.columns([1, 2])

# Columna 1: Gráfico que permanece fijo mientras el texto en la segunda columna se desplaza
with col1:
    st.markdown('<div class="fixed-content">', unsafe_allow_html=True)
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Columna 2: Texto largo que se desplaza
with col2:
    st.header("Sección 1")
    st.write("Este texto se desplaza mientras el gráfico permanece fijo. Aquí puedes poner historias de datos o explicaciones adicionales.")
    st.write("Texto adicional para hacer la sección más larga y asegurar que se puede hacer scroll. " * 50)

    st.header("Sección 2")
    st.write("Continúa con más información y el gráfico sigue siendo fijo en la otra columna.")
    st.write("Texto adicional para hacer la sección más larga y asegurar que se puede hacer scroll. " * 50)

    st.header("Sección 3")
    st.write("Finalmente, esta es la sección final.")
    st.write("Texto adicional para hacer la sección más larga y asegurar que se puede hacer scroll. " * 50)
