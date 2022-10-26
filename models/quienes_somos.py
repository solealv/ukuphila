import streamlit.components.v1 as components
import streamlit as st

def app():

    header_container = st.container()
    dash1_container = st.container()
    dash2_container = st.container()

    with header_container:
        titulo, espacio, imagen = st.columns(3)
        
        titulo.title('Ukuphila +')
        espacio.title('Vida')
        imagen.image('./images/Logo2.png', width= 150)
        
        st.subheader('Significado mas alla de las fronteras')
        st.write('En zulú, la principal lengua materna de Sudáfrica, ukuphila significa vida. Por esta razón, la elegimos como nombre para nuestra ONG.')
        st.subheader('Buscamos datos y los transformamos en informacion.')
        st.write('Desde la ONG Ukuphila + Vida nos planteamos el objetivo de poner en números el desarrollo humano a nivel global. Para esto, ponemos en marcha un proyecto donde nuestro equipo de científicos, analistas e ingenieros de datos buscarán traducir los datos en información para la sociedad.')

    
    with dash1_container:
        titulo, espacio, imagen = st.columns(3)
        
        titulo.title('Esperanza')
        espacio.title('de vida')
        imagen.image('./images/esperanza.png', width= 130)

        st.write('La esperanza de vida se refiere al número de años que en promedio esperaría vivir una persona, si se consideran constantes los indicadores de mortalidad al momento del nacimiento. Se utiliza para medir el nivel de salud general de una población y determinar el desarrollo de ese sector.')
        st.write('Elegimos esta métrica porque la misma es utilizada por el programa de las naciones unidas para el desarrollo (PNUD) como uno de los componentes principales para medir el índice de desarrollo humano (IDH), según este índice se categorizan a todos los estados en cuatro cuartiles muy alto, alto, medio y bajo.')
        st.subheader('¿Cómo se calcula la esperanza de vida?')
        st.write('La esperanza de vida se mide por el promedio de edad de las defunciones en una población durante un intervalo definido de tiempo; anotando la importancia de que a menor mortalidad infantil, mayor esperanza de vida.')
        st.write('La esperanza de vida aparte de ser un indicador de estabilidad en salud pública influye directamente en el crecimiento económico y la inversión internacional en factores de producción tales como el capital humano.')
        
    
    with dash2_container:
        titulo, espacio, imagen = st.columns(3)
        
        titulo.title('> Nuestros')
        espacio.title('objetivos')
        imagen.image('./images/objetivos.png', width= 220)

        st.subheader('Objetivo principal')
        st.write('Identificar la incidencia y manifestación de los principales factores sociales y económicos que tienen correspondencia en la esperanza de vida de una población en un periodo de tiempo y espacio definido.')
        st.subheader('Objetivos generales')
        st.write('* Analizar la evolución histórica de la esperanza de vida en un conjunto de al menos 30 países de diferentes partes del mundo.')
        st.write('* Determinar qué países y/o continentes tienen mejor proyección a futuro con la esperanza de vida.')
        st.write('* Observar y analizar el comportamiento histórico de la esperanza de vida con una antigüedad no menor a 30 años.')
        st.write('* Establecer los principales aspectos económicos, políticos, ambientales, educativos y de salud que tienen relación directa con la esperanza de vida.')
