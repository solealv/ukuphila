import streamlit.components.v1 as components
import streamlit as st

def app():

    header_container = st.container()
    conclusion1_container = st.container()
    conclusion2_container = st.container()
    conclusion3_container = st.container()

    with header_container:
        titulo, espacio, imagen = st.columns(3)
        
        titulo.title('Ukuphila +')
        espacio.title('Vida')
        imagen.image('./images/Logo2.png', width= 150)

    with conclusion1_container:

        st.subheader('La importancia de recorrer este camino')
        

        st.write('Al momento de hacer una visión global del análisis presentado sobre la Esperanza de Vida al Nacer; habiendo explorado los aspectos de estudios elegidos Economía, Salud, Alfabetización, Ambiental y Político, sabemos que la plena comprensión de esta amplia temática es en sí mismo todo un desafío.')
        espacio1, espacio2, imagen1, espacio3, espacio4  = st.columns(5)
        espacio1.write(' ')
        espacio2.write(' ')
        imagen1.image('./images/Crecimiento.png', width= 100)
        espacio3.write(' ')
        espacio4.write(' ')
        st.write('Crear el camino hacia entender cómo sucede que, en el mismo mundo, tengamos brechas tan marcadas en este indicador encontrando países donde hay una media de 50 a 53 años como esperanza de vida al nacer, Lesoto, Chad, Angola, Sierra Leona, y luego tenemos la otra de países como, Japón, Italia, Suiza, Australia, Andorra que trasmiten realidad opuestas. Para evidenciar estos aspectos se requieren de herramientas para tratar los datos que permitan volver visible la información y es de gran importancia que su utilización se difunda. Con proyectos como estos es que se busca una democratización de la información, y se busca que estos lleguen a los puestos de poder que toman las decisiones para trabajar sobre estas realidades.')

    with conclusion2_container:
        espacio1, imagen1,  espacio4  = st.columns(3)
        espacio1.write(' ')
        imagen1.image('./images/poblacion2.png', use_column_width='always')
        espacio4.write(' ')
        st.subheader('Un recorrido por los ejes')
        st.write('Al analizar el aspecto Económico, fue fácil notar las enormes diferencias entre aquellos países denominados de primer mundo o economías fuertes, el ingreso per cápita, los volúmenes de movimientos de divisas en estos países y de los medios de producción que poseen.')
        st.write('Esto inmediatamente nos traslada al eje de mayor impacto Salud. Se observa que se ve altamente afectada la manera en que un país puede ofrecer estructura sanitaria si no dispone de los medios que brindan una economía sana y fuerte. Por esto, no es casualidad que los países con los últimos puestos de este indicador, están el continente africano, quienes menos esperanza de vida, paralelamente son lo que tienen enormes problemas para disponer de agua potable, falta de estructuras sanitarias y sus economías saqueadas sin esquemas de producción para atender las demandas de sus habitantes.')
        st.write('Por otro lado tenemos una economía fuerte como lo es Japón con una infraestructura capaz de iniciar reparaciones, asistir, a supervivientes y hasta disponer de los medios para controlar enormes problemáticas, como el de la planta nuclear luego de ser golpeados por un tsunami el 11 de marzo del 2011.')
        st.write('Girando el globo terráqueo nos encontramos con Haití, que aún hoy está destruido por un evento similar del 10 de enero del 2010 un año antes que el país asiatico, eventos similares poca separación temporal, y los resultados a la vista, una economía fuerte, una estructura sanitaria planificada, sistemas de logística, y tecnología para hacer frente al evento y en el otro caso aún sigue en ruinas.')
        
        espacio1, espacio2, imagen1, espacio3, espacio4  = st.columns(5)
        espacio1.write(' ')
        espacio2.write(' ')
        imagen1.image('./images/poblacion.png', width= 100)
        espacio3.write(' ')
        espacio4.write(' ')
        
        st.write('##### Los impactos mas recientes también son parte de la historia.')
        st.write('Si bien la medición es algo nueva en la historia de la vida humana, luego de lo que pareciera una línea en ascenso, nos encontramos desde el año 2020 con el evento de la pandemia. Se observa que este fenómeno deja ese descenso que notamos en las gráficas de la expectativa de vida, evento conocido por todos y vino a poner a prueba las habilidades humanas para manejar una situación como esta.')
        

    with conclusion3_container:

        espacio1, espacio2, imagen1, espacio3, espacio4  = st.columns(5)
        espacio1.write(' ')
        espacio2.write(' ')
        imagen1.image('./images/AnalisisDatos.png', width= 100)
        espacio3.write(' ')
        espacio4.write(' ')
        
        st.subheader('La tecnologia al servicio.')
        st.write('El desafío para la raza humana, y particularmente para los gobiernos, será la de aplicar todo su conocimiento para avanzar en salud, protección de infantes, protección de madres, suministro de agua potables y estructuras sanitarias, agua potable, hospitales y disposición de medicinas en los países en posición de desigualdad.')
        st.write('Poner la tecnología del análisis y la ciencia de datos al servicio del hombre para prever y anticipar problemas ambientales y climáticos, para crecer en la voluntad política de manera que estos cambios se lleven a cabo. Ya que hemos visto que en un país altamente corrupto esto se ve traducido en un gran porcentaje de su población vive en la pobreza, producto de las malas gestiones por parte de los estados.')
        #st.write('')
        #st.write('')
