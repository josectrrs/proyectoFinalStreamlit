import streamlit as st
from adminPage import adminPage
from auxiliarPage import auxiliarPage
from FAQPage import FAQPage

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

# Mostrar el botón "Ir a Preguntas Frecuentes" en todo momento
if st.button("Ir a Preguntas Frecuentes"):
    FAQPage()

# Determinar la página a mostrar
if st.session_state.username is None:
    login()
else:
    if st.session_state.username == "admin":
        adminPage(st.session_state.username)
    elif st.session_state.username == "auxiliar":
        auxiliarPage(st.session_state.username)
