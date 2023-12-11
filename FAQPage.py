import streamlit as st
from streamlit_option_menu import option_menu

st.title("Preguntas Frecuentes (FAQ) - Proyecto Final")

# 2. horizontal menu
selected2 = option_menu(None, ["Paso 1", "Paso 2", "Paso 3", 'Paso 4'],
                        menu_icon="cast", default_index=0, orientation="horizontal")

# Expander para Paso 1
if selected2 == "Paso 1":
    with st.expander("Ver explicación del Paso 1"):
        st.write("""
            :pencil: **Adquisición de datos** 
            
            :green[**¿Qué datos están trabajando?:**]
            Estamos trabajando con datos de clientes del sistema de "Factura Electrónica de CONTPAQi". Estos datos incluyen información relacionada con los clientes que utilizan el sistema, como sus nombres, Registro Federal de Contribuyentes (RFC), razón social, Régimen Fiscal, Código Postal y otros detalles relevantes. Estos datos son esenciales para la emisión de facturas electrónicas y deben ser validados ante el Servicio de Administración Tributaria (SAT) para asegurar su corrección y cumplimiento con las regulaciones fiscales.

            :green[**¿De dónde se obtuvieron?:**]
            Los datos fueron obtenidos a través de una base de datos de clientes del sistema de Factura Electrónica de CONTPAQi. Esta base de datos contiene información sobre diversas empresas que utilizan el sistema y que han registrado sus datos para la emisión de facturas electrónicas.
            
        """)
        st.image("imgs/CONTPAQiFE.png", caption="Fuente de la obtención de datos", use_column_width=True)
# Expander para Paso 2
elif selected2 == "Paso 2":
    with st.expander("Ver explicación del Paso 2"):
        st.write("""
            :pencil: **Limpieza de los datos** 
            
            La limpieza de datos se llevó a cabo después de obtener un archivo en formato .xlsx de clientes del sistema de Factura Electrónica de CONTPAQi.
            """)
        st.image("imgs/0_PF.png", caption="Archivo en formato .xlsx", use_column_width=True)
        st.write("""
            A continuación, se detallan los pasos de limpieza que se realizaron:
            
            :green[**Carga de Datos:**]
            Se utilizó la biblioteca Pandas para cargar los datos desde el archivo .xlsx a un DataFrame llamado datoClientes.
            """)
        st.image("imgs/1_1PF.png", caption="Carga de Datos", use_column_width=True)
        st.write("""
            :green[**Selección de Columnas Relevantes:**]
            Se eliminaron las columnas innecesarias ("Razón Social", "Régimen Fiscal", "Código Postal") y se conservó solo la columna del RFC. 
            """)
        st.image("imgs/2_PF.png", caption="Selección de Columnas Relevantes", use_column_width=True)
        st.write("""
            :green[**Modificación de Nombres de Columnas:**]
            Se estableció el nombre de la columna que quedaba como 'None' porque en el contexto del análisis posterior este dato no era útil.
            """)
        st.image("imgs/3_PF.png", caption="Modificación de Nombres de Columnas", use_column_width=True)
        st.write("""
            :green[**Formato Específico:**]
            Se agregó el símbolo | al principio de cada valor en el DataFrame, utilizando applymap y una función lambda.
            """)
        st.image("imgs/4_PF.png", caption="Formato Específico", use_column_width=True)
        st.write("""
            :green[**Enumeración:**]
            Añadimos una columna adicional para enumerar las filas al principio del DataFrame datoClientes.
            """)
        st.image("imgs/5_PF.png", caption="Enumeración", use_column_width=True)
        st.write("""
            :green[**Eliminación de Caracteres Especiales:**]
            Eliminamos caracteres no deseados tales como los tabuladores de las filas del DataFrame.
            """)
        st.image("imgs/6_PF.png", caption="Eliminación de Caracteres Especiales", use_column_width=True)
        st.write("""
            :green[**Exportación a Formato Texto (.txt):**]
            Guardamos el DataFrame resultante en un archivo de texto llamado "datos3.txt".
            """)
        st.image("imgs/7_PF.png", caption="Exportación a Formato Texto (.txt)", use_column_width=True)
        st.write("""
            :green[**Lectura y Ajuste Adicional:**]
            Abrimos y leemos una vez más el archivo de texto y guardamos las líneas en la lista "lineas".
            
        """)
        st.image("imgs/9_PF.png", caption="Lectura", use_column_width=True)
        st.write("""
                    **1)** Eliminamos la primera línea de la lista "lineas".
                    
                    **2)** Creamos una lista vacía llamada Lineas2.
                    
                    **3)** Luego Iteramos sobre cada línea en la lista "lineas".
                    
                    **4)** Eliminamos los caracteres de tabulación de cada línea.
                    
                    **5)** Agregamos la línea sin caracteres de tabulación a la lista "Lineas2".

                    **6)** Por último, mostramos la lista "Lineas2" después de eliminar los caracteres de tabulación.
                
        """)
        st.image("imgs/10_PF.png", caption="Lectura", use_column_width=True)

        st.write("""
                    **1)** Abrimos el archivo "datos3.txt" en modo escritura utilizando la declaración with.
                            
                    **2)** Iteramos sobre cada línea en la lista "Lineas2".
                            
                    **3)** Escribimos cada línea en el archivo "datos3.txt" sin caracteres de tabulación.
        """)
        st.image("imgs/11_PF.png", caption="Lectura", use_column_width=True)
        st.write("""
                    :green[**Resultado obtenido:**]
                """)
        st.image("imgs/12_PF.png", caption="Resultado obtenido", use_column_width=True)

# Expander para Paso 3
elif selected2 == "Paso 3":
    with st.expander("Ver explicación del Paso 3"):
        st.write("""
            :pencil: **Análisis de los datos** 
            
            El análisis de datos es una fase crucial en el proceso de ciencia de datos que nos permite extraer información valiosa y patrones significativos de los datos adquiridos y limpiados. 
        """)
        st.write("""
            En este proyecto específico, se llevaron a cabo las siguientes acciones:
        """)

        st.write("""
            :green[**Validación de RFC ante el SAT:**]
            Se utilizó la información de los RFC de los clientes para realizar una validación ante el Servicio de Administración Tributaria (SAT). Esto implica verificar si los RFC son válidos y cumplen con las regulaciones fiscales vigentes.        
        """)
        st.image("imgs/urlValidacion.png", caption="URL del SAT", use_column_width=True)

        st.image("imgs/imgValidacion.png", caption="Página de validación masiva de RFC", use_column_width=True)

        st.image("imgs/respuestaSAT.png", caption="Validación de los RFC obtenida del SAT", use_column_width=True)

# Expander para Paso 4
elif selected2 == "Paso 4":
    with st.expander("Ver explicación del Paso 4"):
        st.write("""
            :pencil: **Visualización de los datos** 
            
            La visualización de datos es esencial para comunicar de manera efectiva los resultados del análisis y proporcionar una comprensión intuitiva de los patrones identificados. En este proyecto, se realizaron las siguientes acciones:
            
            :green[**Qué datos están trabajando:**]
            Estamos trabajando con datos de clientes del sistema d

            
        """)

#selected2



