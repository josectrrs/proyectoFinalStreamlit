import streamlit as st
from streamlit_option_menu import option_menu

st.title("Preguntas Frecuentes (FAQ) - Proyecto Final")

# 2. horizontal menu
selected2 = option_menu(None, ["Paso 1", "Paso 2", "Paso 3", 'Paso 4'],
                        icons=['house', 'cloud-upload', "list-task", 'gear'],
                        menu_icon="cast", default_index=0, orientation="horizontal")

# Expander para Paso 1
if selected2 == "Paso 1":
    with st.expander("Ver explicación del Paso 1"):
        st.write("""
            Aquí va la explicación detallada del Paso 1.
            Puedes agregar texto, imágenes o cualquier otro contenidos.
        """)
# Expander para Paso 2
elif selected2 == "Paso 2":
    with st.expander("Ver explicación del Paso 2"):
        st.write("""
            Aquí va la explicación detallada del Paso 2.
            Puedes agregar texto, imágenes o cualquier otro contenido.
        """)
# Expander para Paso 3
elif selected2 == "Paso 3":
    with st.expander("Ver explicación del Paso 3"):
        st.write("""
            Aquí va la explicación detallada del Paso 3.
            Puedes agregar texto, imágenes o cualquier otro contenido.
        """)
# Expander para Paso 4
elif selected2 == "Paso 4":
    with st.expander("Ver explicación del Paso 4"):
        st.write("""
            Aquí va la explicación detallada del Paso 4.
            Puedes agregar texto, imágenes o cualquier otro contenido.
        """)

selected2



