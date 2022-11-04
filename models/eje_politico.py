import streamlit.components.v1 as components
import streamlit as st


def app():

    header_container = st.container()
    intro_container =  st.container()
    dash1_container = st.container()

    with header_container:
        titulo, espacio, imagen = st.columns(3)
        
        titulo.title('Ukuphila +')
        espacio.title('Vida')
        imagen.image('./images/Logo2.png', width= 150)

    with intro_container:

            st.subheader('Abordaje del analisis')
            st.write('Al momento de analizar el eje político, se presenta una paridad entre aquellos países que no gozan de los mejores indicadores en la expectativa de vida, coincidentemente en varios de ellos la información es escasa, o casi nula. Se utilizó como fuente principal de información la base de datos pública del Banco Mundial, en donde una de las fuentes hace referencia a un indicador que trata sobre la calificación de transparencia, responsabilidad y corrupción en el sector público.')
            st.write('Aquí la fuente evalúa hasta qué punto el Poder Ejecutivo es responsable del uso de los fondos y del resultado de sus acciones ante el electorado y los poderes Legislativo y Judicial y en qué medida se exige a los empleados públicos que conforman el Poder Ejecutivo que rindan cuentas de las decisiones administrativas, el uso de los recursos y los resultados obtenidos.')
            st.write('El identificador para esta métrica  se lo llama Estimate y se refiere a eficacia y fortaleza de gobierno. Toma los valores en un rango de -2.5 (débil) a 2.5 (fuerte) de la performance de gobierno.')


    with dash1_container:
        st.subheader('Control de Corrupción y Esperanza de vida')
        st.write('Rank es el ranking entre países de acuerdo a su calificación. Se procede a mostrar como este parametro se relaiona con el indicador objetivo.')
        components.iframe('https://app.powerbi.com/view?r=eyJrIjoiNzcyMDdlOWEtY2Q3YS00ZDJhLWFiNzYtZmQ0ZTYwMDY0MmZiIiwidCI6IjE4OWJmYzRlLWY3ZjEtNGEzZC04MjhhLWU2NDM0ZmMxZjJlNyJ9', height=450)
