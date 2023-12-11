import streamlit as st
from adminPage import adminPage
from auxiliarPage import auxiliarPage
from streamlit_option_menu import option_menu


with st.sidebar:
    selected = option_menu("Menú Principal", ["Login", 'FAQ'],
        icons=['house', 'gear'], menu_icon="cast", default_index=0)

if selected == "Login":
    # Función para verificar las credenciales
    def authenticate(username, password):
        # Usuarios estáticos sin base de datos
        users = {
            "admin": "admin",
            "auxiliar": "auxiliar"
        }

        # Verificar si las credenciales son correctas
        if username in users and users[username] == password:
            return True
        else:
            return False


    # Página de login
    def login():
        st.title("Inicio de Sesión")
        username = st.text_input("Usuario")
        password = st.text_input("Contraseña", type="password")

        if st.button("Iniciar Sesión"):
            if authenticate(username, password):
                st.success(f"Bienvenido, {username}!")
                st.session_state.username = username  # Almacenar el nombre de usuario en la sesión
                login_container.empty()  # Eliminar el panel de inicio de sesión
                st.experimental_rerun()  # Recargar la aplicación para mostrar la página correspondiente
            else:
                st.error("Credenciales incorrectas")


    # Verificar si el usuario ha iniciado sesión
    if "username" not in st.session_state:
        st.session_state.username = None

    # Crear un contenedor para el panel de inicio de sesión
    login_container = st.empty()

    # Determinar la página a mostrar
    if st.session_state.username is None:
        login()
    else:
        if st.session_state.username == "admin":
            adminPage(st.session_state.username)
        elif st.session_state.username == "auxiliar":
            auxiliarPage(st.session_state.username)
elif selected == "FAQ":
    st.title("Preguntas Frecuentes (FAQ) - Proyecto Final")

    st.write("""
        :pencil: **Adquisición de datos** 

        :green[**¿Qué datos están trabajando?:**]
        Estamos trabajando con datos de clientes del sistema de "Factura Electrónica de CONTPAQi". Estos datos incluyen información relacionada con los clientes que utilizan el sistema, como sus nombres, Registro Federal de Contribuyentes (RFC), razón social, Régimen Fiscal, Código Postal y otros detalles relevantes. Estos datos son esenciales para la emisión de facturas electrónicas y deben ser validados ante el Servicio de Administración Tributaria (SAT) para asegurar su corrección y cumplimiento con las regulaciones fiscales.

        :green[**¿De dónde se obtuvieron?:**]
        Los datos fueron obtenidos a través de una base de datos de clientes del sistema de Factura Electrónica de CONTPAQi. Esta base de datos contiene información sobre diversas empresas que utilizan el sistema y que han registrado sus datos para la emisión de facturas electrónicas.

    """)
    st.image("imgs/CONTPAQiFE.png", caption="Fuente de la obtención de datos", use_column_width=True)



