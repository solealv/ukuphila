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
        st.write('Para el análisis del sector salud se utilizó como principal fuente de datos la proveniente del Banco Mundial. Se agruparon los mismos por temas y se analizó la relación entre cada indicador extraído y la esperanza de vida.')
        st.write('Los resultados arrojaban una fuerte correlacion entre la esperanza e vida con Gastos en salud, Tasa de mortalidad en adultos, Tasa de mortalidad en infantes y la Tasa de fertilidad')
        st.write('En los siguientes reportes interactivos se puede observar en mayor detalle estos indicadores destacados')

    with dash1_container:
        st.subheader('Gastos en salud')
        st.write('La revisión desde el punto de vista económico para el eje salud abordó una ventana temporal de 60 años y dos conjuntos de datos. Por una parte el gasto sanitario de las administraciones públicas nacionales expresado como porcentaje del PIB y por otra parte el gasto sanitario corriente per cápita expresado en dólares corrientes.')
        
        ########################## dashboard ############################
        components.iframe('https://app.powerbi.com/view?r=eyJrIjoiNWM0NzM2MDgtMmZkOS00MDYwLTgzNTctNmJiZmFmNGYxOTE5IiwidCI6IjE4OWJmYzRlLWY3ZjEtNGEzZC04MjhhLWU2NDM0ZmMxZjJlNyJ9&pageName=ReportSection12e7e61b65ed10477328', height=450)
        ########################## dashboard ############################
        
        st.write('##### Observaciones')
        st.write('En cuanto al gasto de las administraciones públicas nacionales, destaca en primer lugar Alemania y países europeos, además, es de especial interés que destacan en este pequeño grupo Estados Unidos, Japón y Canadá. De manera similar a la tendencia mostrada por la serie de datos anterior, en lo que respecta al gasto corriente, sobresalen en gran medida Estados Unidos y Suiza, con valores de 2493 y 2366 dólares corrientes.')
        st.write('El promedio de los 33 países analizados para el gasto público nacional y corriente es de 1.31% y 561.72 dólares corrientes. Si bien Suiza no tiene un gran capital destinado al gasto sanitario de las administraciones públicas es bastante importante la inversión en salud respecto al gasto corriente per cápita.')
        st.write('Una revisión con una ventana temporal más reciente (2001 a 2021) mantiene la misma tendencia descrita anteriormente, con Japón y Suiza en el top 5 de países con mayor esperanza de vida.')
        st.write('El sistema de salud japonés se basa en un único seguro obligatorio universal, con cobertura médica y odontológica. El sistema de salud en Suiza al igual que en Estados Unidos es mixto, público pero preponderadamente privado y de alto costo.')

        
    with dash2_container:
        st.subheader('Mortalidad y fertilidad')
        st.write('En lo que respecta al análisis de mortalidad, también se utilizó una ventana temporal de 60 años, segmentada por edades, hombres y mujeres adultas, niños y niñas menores de 5 años, 1 año y neonatos con menos de 28 días de nacidos.')
        
        ########################## dashboard ############################
        components.iframe('https://app.powerbi.com/view?r=eyJrIjoiNWM0NzM2MDgtMmZkOS00MDYwLTgzNTctNmJiZmFmNGYxOTE5IiwidCI6IjE4OWJmYzRlLWY3ZjEtNGEzZC04MjhhLWU2NDM0ZmMxZjJlNyJ9&pageName=ReportSection817da2788864c5a49e89', height=450)
        ########################## dashboard ############################
        
        st.write('##### Observaciones')
        st.write('Para todos los países mueren en su mayoría hombres adultos, seguido de mujeres adultas y luego niños y niñas menores de 5 años. Estos valores son preponderantes en los países de África y destaca Afganistán. Los países con menor mortalidad en todos los rangos etarios son Japón, Países Bajos y Alemania. Con una ventana temporal más reciente (2001 a 2021) se ubica Italia como el país con menor mortalidad, los demás hallazgos se mantienen iguales.')
        st.write('En cuanto a fertilidad, se analizaron dos conjuntos de datos, la tasa de fertilidad en adolescentes respecto a la cantidad de nacimientos por cada mil mujeres con edades entre 15 y 19 años; para este caso, destacan en África, Nigeria, Camerún y Angola, con las tasas más altas de fertilidad, seguido de Afganistán y luego preponderancia de países de Suramérica; los menores valores se observan en Corea del Sur, Suiza y Japón.')
        st.write('Respecto a la tasa de fertilidad total medida en nacimientos por mujer y en una ventana temporal de 60 años, el país más fértil de los analizados es Afganistán, seguido de países africanos y suramericanos, en el otro extremo están Alemania, Japón e Italia.')
        st.write('Para los últimos 20 años, las mayores tasas de fertilidad se mantienen en los mismos países; sin embargo, el top 3 de menor tasa se asigna a Corea del Sur, España y Ucrania, seguido de los tres descritos en la anterior ventana temporal.')
        st.write('Otro elemento de análisis es la brecha entre la esperanza de vida entre hombres y mujeres adultos, este valor es mayor en Rusia, Ucrania y Corea del Sur con valores de 10.81, 9.21, y 7.41 años. En los últimos años, la brecha temporal aumentó para Rusia y Ucrania y países de Sudamérica. Los menores valores se observan en Nigeria e India.')
        
        st.subheader('Conclusiones')
        st.write('La conclusión observada en los gráficos indicados, es que hay una relación directa entre la esperanza de vida y la asignación de recursos económicos para la salud. Por lo anterior, la gran mayoría de países africanos se encuentran en los lugares más bajos de esperanza de vida y gasto sanitario público nacional y corriente; haciendo mención al caso especial de Afganistán estado en guerra por décadas.')
