# adminPage.py
import streamlit as st
import pandas as pd
import os

def adminPage(username):
    st.title(f"Panel de Administrador - Bienvenido, {username}")
    st.write("Acciones específicas para administradores")

    # Subir archivo Excel
    excel_file = st.file_uploader("Subir archivo Excel", type=["xls", "xlsx"])
    if excel_file is not None:
        # Obtener el nombre original del archivo
        excel_filename = excel_file.name
        save_path = os.path.join("archivos", excel_filename)

        # Guardar el archivo Excel en la carpeta "archivos"
        with open(save_path, "wb") as excel_file_save:
            excel_file_save.write(excel_file.getvalue())

        excel_df = pd.read_excel(save_path)
        st.success("Archivo Excel subido con éxito!")

        # Leer el archivo Excel y mostrar su contenido en una tabla
        st.write("Contenido del archivo Excel:")
        st.write(excel_df)

    # Subir archivo de texto
    txt_file = st.file_uploader("Subir archivo de texto", type=["txt"])
    if txt_file is not None:
        # Obtener el nombre original del archivo
        txt_filename = txt_file.name
        save_path = os.path.join("archivos", txt_filename)

        # Guardar el archivo de texto en la carpeta "archivos"
        with open(save_path, "wb") as txt_file_save:
            txt_file_save.write(txt_file.getvalue())

        txt_content = txt_file.getvalue().decode("latin-1")
        st.success("Archivo de texto subido con éxito!")

        # Mostrar el contenido del archivo de texto en una tabla
        st.write("Contenido del archivo de texto:")
        st.write(txt_content)

    # Botón para cerrar sesión
    if st.button("Cerrar Sesión"):
        st.session_state.username = None  # Asignar un valor nulo al nombre de usuario
        st.experimental_rerun()  # Recargar la aplicación para mostrar la página de inicio de sesión
