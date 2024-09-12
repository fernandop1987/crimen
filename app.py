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
col1, col2 = st.columns([1, 1])

# Columna 1: Gráfico que permanece fijo mientras haces scroll en la columna 2
with col1:
    st.plotly_chart(fig, use_container_width=True)

# Columna 2: Contenido que se desplaza al hacer scroll
with col2:
    # CSS para mantener el gráfico en la columna 1 fijo
    st.markdown("""
    <style>
    .fixed-content {
        position: -webkit-sticky; /* Safari */
        position: sticky;
        top: 0;
    }
    .scroll-container {
        height: 100vh;
        overflow-y: scroll;
    }
    </style>
    """, unsafe_allow_html=True)

    # Texto que se mueve con el scroll
    st.markdown("""
    <div class="scroll-container">
        <h2>Sección 1</h2>
        <p>Este texto se desplaza mientras el gráfico permanece fijo. Puedes seguir haciendo scroll para ver más contenido. Aquí puedes poner historias de datos o explicaciones adicionales.</p>

        <h2>Sección 2</h2>
        <p>Cuando llegues a esta sección, puedes continuar describiendo tus datos o agregar más visualizaciones. La columna de la derecha puede seguir mostrando gráficos fijos o información relevante.</p>

        <h2>Sección 3</h2>
        <p>Finalmente, puedes cerrar tu historia en esta sección y dejar que el usuario continúe navegando por el contenido de la página. Esta es una estrategia muy útil para historias con varios puntos de datos.</p>
    </div>
    """, unsafe_allow_html=True)


# Footer o información adicional
st.markdown("---")
st.write("Creado por ABCData. Todos los derechos reservados.")
