# adminPage.py
import streamlit as st
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

        st.success("Archivo Excel subido con éxito!")

    # Subir archivo de texto
    txt_file = st.file_uploader("Subir archivo de texto", type=["txt"])
    if txt_file is not None:
        # Obtener el nombre original del archivo
        txt_filename = txt_file.name
        save_path = os.path.join("archivos", txt_filename)

        # Guardar el archivo de texto en la carpeta "archivos"
        with open(save_path, "wb") as txt_file_save:
            txt_file_save.write(txt_file.getvalue())

        st.success("Archivo de texto subido con éxito!")



    # Mostrar archivos en la carpeta "archivos"
    st.write("Archivos en la carpeta 'archivos':")
    archivos_en_carpeta = [file for file in os.listdir("archivos") if file.endswith((".xls", ".xlsx", ".txt"))]

    if not archivos_en_carpeta:
        st.warning("No se encontraron archivos en la carpeta 'archivos'.")
    else:
        st.write(archivos_en_carpeta)

    # Botón para vaciar archivos .xlsx, .xls y .txt
    if st.button("Vaciar Archivos"):
        archivos_a_eliminar = [file for file in os.listdir("archivos") if file.endswith((".xls", ".xlsx", ".txt"))]
        for archivo in archivos_a_eliminar:
            archivo_path = os.path.join("archivos", archivo)
            os.remove(archivo_path)

        st.success("Archivos .xlsx, .xls y .txt eliminados con éxito!")

    # Botón para cerrar sesión
    if st.button("Cerrar Sesión"):
        st.session_state.username = None  # Asignar un valor nulo al nombre de usuario
        st.experimental_rerun()  # Recargar la aplicación para mostrar la página de inicio de sesión
