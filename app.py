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

# Insertamos el CSS y JavaScript necesarios para ScrollyTeller
st.markdown("""
    <script src="https://cdn.jsdelivr.net/gh/ihmeuw/ScrollyTeller@0.0.2/src/scrollyteller.js"></script>
    <style>
    .scrolly-container {
        display: flex;
        justify-content: space-between;
    }
    .scrolly-text {
        width: 50%;
        height: 100vh;
        overflow-y: scroll;
    }
    .scrolly-graphic {
        width: 40%;
        height: 100vh;
        position: sticky;
        top: 0;
    }
    .step {
        margin-bottom: 100vh;
    }
    </style>
    
    <div class="scrolly-container">
        <div class="scrolly-text" id="scrolly-text">
            <div class="step">
                <h2>Sección 1</h2>
                <p>Este es el primer bloque de texto. Al hacer scroll, el gráfico permanece fijo.</p>
            </div>
            <div class="step">
                <h2>Sección 2</h2>
                <p>Más texto mientras sigues desplazándote. El gráfico sigue fijo en la columna derecha.</p>
            </div>
            <div class="step">
                <h2>Sección 3</h2>
                <p>Última sección, donde puedes agregar más detalles sobre los datos o la visualización.</p>
            </div>
        </div>
        <div class="scrolly-graphic" id="scrolly-graphic">
            <!-- Aquí cargaremos el gráfico de Plotly -->
        </div>
    </div>

    <script>
    document.addEventListener("DOMContentLoaded", function() {
        const scrolly = new ScrollyTeller({
            parent: document.querySelector("#scrolly-text"),
            triggerTop: 1/3, // La posición en la que se activará cada paso
            triggerTopMobile: 0.75, // Ajustes para móviles
            transparentUntilActive: true
        });

        scrolly.addTrigger({
            num: 1,
            do: () => {
                // Aquí puedes cambiar el gráfico o mostrar algo cuando llegues al paso 1
                document.querySelector("#scrolly-graphic").innerHTML = "Gráfico en Sección 1";
            }
        });

        scrolly.addTrigger({
            num: 2,
            do: () => {
                // Cambio cuando llegas al paso 2
                document.querySelector("#scrolly-graphic").innerHTML = "Gráfico en Sección 2";
            }
        });

        scrolly.addTrigger({
            num: 3,
            do: () => {
                // Cambio cuando llegas al paso 3
                document.querySelector("#scrolly-graphic").innerHTML = "Gráfico en Sección 3";
            }
        });
    });
    </script>
    """, unsafe_allow_html=True)

# Insertamos el gráfico Plotly en la posición correcta
st.plotly_chart(fig, use_container_width=True)
