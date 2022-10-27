import streamlit.components.v1 as components
import streamlit as st


def app():
    
    header_container = st.container()
    intro_container = st.container()
    dash1_container = st.container()
    dash2_container = st.container()
    dash3_container = st.container()
    
    with header_container:
        titulo, espacio, imagen = st.columns(3)
        
        titulo.title('Ukuphila +')
        espacio.title('Vida')
        imagen.image('./images/Logo2.png', width= 150)

    with intro_container:
        st.subheader('Abordaje del analisis')
        st.write('Dentro del eje Educación se trabajó con la la base de datos del Banco Mundial, y se analizó el porcentaje de alfabetización y el porcentaje de población de +25 años con secundario terminado. El primero se eligió porque esto es el resultado de un proceso continuo de aprendizaje y conocimiento de la lectura, la escritura y el uso de los números a lo largo de la vida, y forma parte de un conjunto más amplio de competencias, que incluyen las competencias digitales, la alfabetización mediática, la educación para el desarrollo sostenible y la ciudadanía mundial, así como las competencias específicas para el trabajo.')
        st.write('El segundo se eligió por ser el nivel mínimo de estudios que facilita el acceso a la inserción laboral con condiciones dignas. Esto permite establecer un piso educativo en el cual las personas pueden acceder a condiciones de vida aceptables que les permita desarrollo de vida con acceso a los recursos mínimos e indispensables para la subsistencia.')
        st.write('En el eje ambiental se trabajó tanto con la base de datos del Banco mundial como con otras fuentes. Por un lado, se analizó el impacto de la disponibilidad de agua dulce por país. El agua dulce es un recurso escencial para asegurar el acceso a agua potable y generación de alimentos de forma segura, lo cual es fundamental para un desarrollo de vida saludable.')
        st.write('Por otro lado se trabajó con datos referentes al resultado de un estudio donde se analizó el impacto de los desastres naturales y se obtuvo el porcentaje de población que resulta afectada por los mismos. Este involucra todo tipo de fenómenos como sequías, inundaciones, huracanes, tsunamis, etc.')
        st.write('Por último, dentro de este eje se trabajó con El Índice de Desempeño Ambiental (EPI). Este proporciona un resumen basado en datos del estado de la sostenibilidad en todo el mundo. Utilizando 40 indicadores de desempeño en 11 categorías temáticas, el EPI clasifica a los países en el desempeño del cambio climático, la salud ambiental y la vitalidad del ecosistema.')
        st.write('Las clasificaciones generales de EPI indican qué países están abordando mejor los desafíos ambientales que enfrenta cada nación y puede ayudar a comprender los determinantes del progreso ambiental y refinar las opciones de políticas a instrumentar.')
        st.write('Se califica a estos países según su desempeño ambiental utilizando el año más reciente de datos disponibles y calculando cómo han cambiado estos puntajes durante la década anterior.')

    with dash1_container:
        st.subheader('Alfabetizacion y secundario finalizado.')
        
        components.iframe('https://app.powerbi.com/view?r=eyJrIjoiZDc1MTFmZDUtN2U0MC00N2FiLTkzNDctZmZjMWVhMDhhYTE2IiwidCI6IjE4OWJmYzRlLWY3ZjEtNGEzZC04MjhhLWU2NDM0ZmMxZjJlNyJ9&pageName=ReportSection8193aa4cb67e187b0792', height=450)
        
        st.write('##### Observaciones')
        st.write('Más del 90% de la población mundial sabe leer y escribir, con respecto a un 68% en 1979. A pesar de ello, en todo el mundo hay, al menos, 771 millones de jóvenes y adultos que no saben leer ni escribir, dos tercios de ellos son mujeres, así como 250 millones de niños que no adquieren las competencias básicas en lectoescritura.')
        st.write('Observamos que a nivel mundial, los datos se encuentran más actualizados hasta 2019 mostrando a Italia como el país que mayor porcentaje tiene de mayores de 15 años que saben leer y escribir (99,35%) y al final de la tabla encontramos a Afganistán con un 37,27 %.')
        st.write('En cuanto a los mayores de 25 años con secundario completo, Ecuador indica casi un 91% con ese nivel de estudios, mientras que Afganistán vuelve a aparecer con los niveles más bajos, un 9.5 %.')
        st.write('Es también llamativo que, una primera potencia como China, no cuente con información en lo que a educación se refiere disponible en las bases de datos del banco mundial de los últimos 10 años.')
         
    with dash2_container:
        st.subheader('Agua dulce y desastres naturales')
        st.write('Los recursos hídricos gestionados adecuadamente son un componente crítico del crecimiento, la reducción de la pobreza y la equidad. Los medios de subsistencia de los más pobres están relacionados de manera crítica con el acceso a los servicios de agua. Una escasez de agua en el futuro sería perjudicial para la población humana, ya que afectaría todo, desde el saneamiento hasta la salud en general y la producción de cereales.')
        
        components.iframe('https://app.powerbi.com/view?r=eyJrIjoiZDc1MTFmZDUtN2U0MC00N2FiLTkzNDctZmZjMWVhMDhhYTE2IiwidCI6IjE4OWJmYzRlLWY3ZjEtNGEzZC04MjhhLWU2NDM0ZmMxZjJlNyJ9&pageName=ReportSectiona0dd748aea07b3676930', height=450)
        
        st.write('##### Observaciones')
        st.write('Cuantificamos los metros cúbicos de agua dulce disponibles per cápita comprobando cómo ha ido disminuyendo a través del tiempo.')
        st.write('Según datos de 2018, mientras que en Colombia se disponen de casi 77 mil m3 de agua dulce per cápita, Francia muestra solo 638 m3 per cápita. En sexta posición  de tabla encontramos a Argentina y en octava posición a Estados Unidos ambos con unos 27 mil m3 de agua dulce per cápita.')
        st.write('En un análisis macro, observamos que la disponibilidad mundial de agua dulce ha disminuido un 35% en los últimos 50 años.')
        st.write('A nivel mundial, 0.7 % de la población se ve afectada por algún desastre natural. Pero analizando por país, encontramos a China  con un casi 8% de su población afectada y a India con 4.36 %')
        st.write('De los países analizados, Nigeria aparece al final de la tabla con solo 0,06 % de población que sufre consecuencias debido a algún desastre natural.')
        st.write('En lo que a América se refiere, Colombia muestra un 0,66 % de personas afectadas y Argentina un 0,17%.')


    with dash3_container:
        st.subheader('Indice de desempeño ambiental')
        st.write('Se califica a estos países según su desempeño ambiental utilizando el año más reciente de datos disponibles y calculando cómo han cambiado estos puntajes durante la década anterior.')

        components.iframe('https://app.powerbi.com/view?r=eyJrIjoiZDc1MTFmZDUtN2U0MC00N2FiLTkzNDctZmZjMWVhMDhhYTE2IiwidCI6IjE4OWJmYzRlLWY3ZjEtNGEzZC04MjhhLWU2NDM0ZmMxZjJlNyJ9&pageName=ReportSection2698a4100fda16d365e9', height=450)
        
        st.write('##### Observaciones')
        st.write('De los países que abarcan este estudio, con mejor desempeño encontramos a Reino Unido con un  score de casi 78 puntos, mientras que India aparece última con menos de 19.')
        st.write('Observamos también, una llamativa mejora en el score en el caso de Afganistán que, aunque se encuentra a mitad de tabla, muestra un aumento de casi 24 puntos con respecto a los datos de la década anterior.')
        st.write('En latinoamérica, México es el país que más aumentó el score del último EPI, siendo calificado con 45.5 mostrando un aumento de 12 puntos con respecto a los 10 años anteriores.')
        
        st.write('##### Conclusiones')
        st.write('Dado que el objetivo principal de este trabajo es comprobar si existe correlación o no entre los ejes seleccionados y la esperanza de vida, observamos que exite una correlacion entre los valores de los inicadores analizados y la esperanza de vida.')
        st.write('Un ejemplo claro para evidenciar esta relacion se obtiene cuando tomamos un país como Reino Unido que es el mejor posicionado en el  el índice de desempeño ambiental  con un aumento de 24 puntos en la última década y es el tercer  país con mayor tasa de alfabetización en mayores de 25 años cuenta con una esperanza de vida de 83.5 años.')
        st.write('Por otro lado, India, que en cuanto a tasa de alfabetización se encuentra 12 posiciones por debajo y en cuanto al  índice de desempeño ambiental, es el peor posicionado, tiene una esperanza de vida de  11 años menos comparado con el Reino Unido.')