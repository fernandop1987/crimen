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

# Creamos una fila con dos columnas
col1, col2 = st.columns([1, 2])

# Columna 1: Gráfico que permanece fijo
with col1:
    st.markdown("""
    <style>
    .fixed-content {
        position: sticky;
        top: 0;
    }
    </style>
    """, unsafe_allow_html=True)

    # Contenedor fijo para el gráfico
    st.markdown('<div class="fixed-content">', unsafe_allow_html=True)
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Columna 2: Contenido desplazable
with col2:
    # Contenido de la historia con texto desplazable usando las funciones nativas de Streamlit
    st.header("Sección 1")
    st.write("Este texto se desplaza mientras el gráfico permanece fijo. Puedes seguir haciendo scroll para ver más contenido. Aquí puedes poner historias de datos o explicaciones adicionales.")

    st.header("Sección 2")
    st.write("Cuando llegues a esta sección, puedes continuar describiendo tus datos o agregar más visualizaciones. La columna de la derecha puede seguir mostrando gráficos fijos o información relevante.")

    st.header("Sección 3")
    st.write("Finalmente, puedes cerrar tu historia en esta sección y dejar que el usuario continúe navegando por el contenido de la página. Esta es una estrategia muy útil para historias con varios puntos de datos.")

    st.header("Sección 4")
    st.write("Añade más secciones según sea necesario. El contenido seguirá desplazándose mientras el gráfico permanece fijo a la izquierda.")
