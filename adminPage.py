# adminPage.py
import streamlit as st
import pandas as pd
import os

def adminPage(username):
    st.title(f"Panel de Administrador - Bienvenido, {username}")
    st.write("Acciones específicas para administradores")

    # Validar existencia de archivos en la carpeta "archivos"
    excel_files = [file for file in os.listdir("archivos") if file.endswith((".xls", ".xlsx"))]
    txt_files = [file for file in os.listdir("archivos") if file.endswith(".txt")]

    if not excel_files and not txt_files:
        st.warning("No se encontraron archivos .xlsx ni archivos .txt en la carpeta 'archivos'.")
    else:
        # Mostrar archivos .xlsx
        if excel_files:
            st.write("Archivos Excel encontrados:")
            for excel_file in excel_files:
                st.write(excel_file)

        # Mostrar archivos .txt
        if txt_files:
            st.write("Archivos de texto encontrados:")
            for txt_file in txt_files:
                st.write(txt_file)

        # Subir archivo Excel solo si no hay archivos .xlsx
        if not excel_files:
            excel_file = st.file_uploader("Subir archivo Excel", type=["xls", "xlsx"])
            if excel_file is not None:
                excel_filename = excel_file.name
                save_path = os.path.join("archivos", excel_filename)
                with open(save_path, "wb") as excel_file_save:
                    excel_file_save.write(excel_file.getvalue())
                excel_df = pd.read_excel(save_path)
                st.success("Archivo Excel subido con éxito!")
                st.write("Contenido del archivo Excel:")
                st.write(excel_df)

        # Subir archivo de texto solo si no hay archivos .txt
        if not txt_files:
            txt_file = st.file_uploader("Subir archivo de texto", type=["txt"])
            if txt_file is not None:
                txt_filename = txt_file.name
                save_path = os.path.join("archivos", txt_filename)
                with open(save_path, "wb") as txt_file_save:
                    txt_file_save.write(txt_file.getvalue())
                txt_content = txt_file.getvalue().decode("latin-1")
                st.success("Archivo de texto subido con éxito!")
                st.write("Contenido del archivo de texto:")
                st.write(txt_content)

    # Botón para cerrar sesión
    if st.button("Cerrar Sesión"):
        st.session_state.username = None
        st.experimental_rerun()
