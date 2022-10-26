import streamlit.components.v1 as components
import streamlit as st


def app():

    header_container = st.container()
    intro_container = st.container()
    dash1_container = st.container()
    dash2_container = st.container()

    with header_container:
        titulo, espacio, imagen = st.columns(3)
        
        titulo.title('Ukuphila +')
        espacio.title('Vida')
        imagen.image('./images/Logo2.png', width= 150)
        
    with intro_container:
        st.subheader('Abordaje del analisis')
        st.write('Analizamos los distintos factores económicos que creemos afectan con mayor impacto en la expectativa de vida al nacer, los factores y sus datos en su mayoría fueron obtenidos de la principal fuente que fue la API del Banco Mundial y fuentes externas, dentro de una ventana temporal de 60 años.')
        st.write('Entre los factores que se destacaron en su relación con la esperanza de vida se encontraba el Producto Bruto Interno (PIB). Esto resulta razonable ya que este representa la totalidad de producción y consumo de un país definido en un periodo de tiempo. Por esto es que se decide profundizar el análisis sobre este indicador y desglosarlo en los diferentes sectores que aportan a este valor: servicios, agricultura, manufactura e industria.')
        st.write('A su vez, incluimos el indicador deuda externa en porcentaje de PIB. En países en vías de desarrollo la deuda externa puede desestabilizar a un país en caso de que no se lleguen a cumplir con los acuerdos pactados internacionalmente, generando complejas problemáticas a nivel político y económico. La deuda externa representa la suma de la deuda contraída por agentes privados y deuda externa adquirida por el gobierno del país.')

    with dash1_container:
        st.subheader('PIB y desglose')
        
        components.iframe('https://app.powerbi.com/view?r=eyJrIjoiNTU3NjM5NWQtZjU0ZC00MDgxLWIyZjMtNjRkMjdjNTI3MzA5IiwidCI6IjE4OWJmYzRlLWY3ZjEtNGEzZC04MjhhLWU2NDM0ZmMxZjJlNyJ9&pageName=ReportSection', height=450)
        
        st.write('##### Observaciones')
        st.write('Se puedo observar que los países con crecimiento en su PIB ha generado a su vez una mejora en la expectativa de vida. Si tomamos el ejemplo de China, en el año de 1980, su PIB era de 191 mil millones de dólares y su PIB Per Cápita de aproximadamente 195 dólares. A su vez, nos muestra las actividades económicas de su población, la cual se observa que gran parte se debía a los ingresos por la agricultura.')
        st.write('Si se adelanta en el tiempo a un año cercano a la actualidad, ya en el 2020 se evidencia una diferencia y podemos notar que hubo un cambio significativo en todos los indicadores, pasó a ser la segunda economía en términos de PIB, en comparación con las otras seleccionadas, solo después de EEUU, aumentó su PIB Per Cápita a 10500 dólares aproximadamente. Eso se observa que fue acompañado por un cambio en sus actividades económicas.')
        
    with dash2_container:
        st.subheader('PIB y Esperanza de vida')

        components.iframe('https://app.powerbi.com/view?r=eyJrIjoiNTU3NjM5NWQtZjU0ZC00MDgxLWIyZjMtNjRkMjdjNTI3MzA5IiwidCI6IjE4OWJmYzRlLWY3ZjEtNGEzZC04MjhhLWU2NDM0ZmMxZjJlNyJ9&pageName=ReportSection', height=450)
        
        st.write('##### Observaciones')
        st.write('Al ver la evolución de las animaciones se observa como la expectativa de vida se incrementa con el tiempo, y siguiendo nuestro ejemplo, el país China, logró elevar su expectativa de vida al nacer por hombre y por mujer por alrededor de 20 años, y esto va acompañado del alto crecimiento de su PIB y su PIB Per Cápita por lo es notorio la gran correlación que tienen estas variables.')
        st.write('##### Conclusiones')
        st.write('Como ya se mencionó previamente, el PIB es un valor que mide la capacidad productiva de un país. Es lógico esperar que a mayor capacidad productiva, las personas tendrán mejores oportunidades para su desarrollo en su estilo de vida. Se puede observar que el aumento en el PIB va de la mano con el de la esperanza de vida, demostrando que este parámetro es indispensable para el desarrollo humano y el aumento en la expectativa y calidad de vida.')
        st.write('A su vez, se observó que el aporte que genera al PIB el sector servicio es el que mayor correlacion tiene con la esperanza de vida: crece el aporte al PIB desde el sector servicios y crece la esperanza de vida. Para que una sociedad pueda aumentar lo que se genera desde el sector servicios, precisa de desarrollos tecnológicos y educativos que genere una infraestructura para el crecimiento de este sector. Por esto es que es de esperar que sea el que mas infuencia genera en la esperanza de vida.')