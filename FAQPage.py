import streamlit as st
from streamlit_option_menu import option_menu

st.title("Preguntas Frecuentes (FAQ) - Proyecto Final")

# 2. horizontal menu
selected2 = option_menu(None, ["Paso 1", "Paso 2", "Paso 3", 'Paso 4'],
                        icons=['house', 'cloud-upload', "list-task", 'gear'],
                        menu_icon="cast", default_index=0, orientation="horizontal")
selected2



