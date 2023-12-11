# auxiliarPage.py
import streamlit as st
import pandas as pd
import os


# Función para buscar el RFC en el archivo de texto y mostrar el resultado con colores
def buscar_rfc_en_archivo_txt(excel_df, selected_reason_social, txt_content):
    rfc_column = excel_df.loc[excel_df["Razón Social"] == selected_reason_social, "R.F.C."]
    if not rfc_column.empty:
        rfc_to_search = rfc_column.iloc[0]

        # Buscar el RFC correspondiente en el archivo de texto
        lines = txt_content.split('\n')
        for line in lines:
            parts = line.split('|')
            if len(parts) == 3 and parts[1] == rfc_to_search:
                status_text = parts[2].strip()
                if "RFC válido" in status_text:
                    #st.success(f"RFC {rfc_to_search} es válido ante el SAT. Detalles:\n{line}")

                    # Obtener Régimen Fiscal y Código Postal del RFC desde el archivo Excel
                    regimen_fiscal = excel_df.loc[excel_df["R.F.C."] == rfc_to_search, "Régimen Fiscal"].iloc[0]
                    codigo_postal = int(excel_df.loc[excel_df["R.F.C."] == rfc_to_search, "Código Postal"].iloc[0])

                    # Mostrar los datos en una tabla
                    st.write("Detalles del RFC:")
                    df_details = pd.DataFrame({"R.F.C.": [rfc_to_search], "Régimen Fiscal": [regimen_fiscal],
                                               "Código Postal": [codigo_postal], "Respuesta del SAT": [status_text]})
                    st.dataframe(df_details.style.applymap(color_cell, subset=["Respuesta del SAT"]))
                elif "no registrado en el padrón de contribuyentes" in status_text:
                    #st.error(f"RFC {rfc_to_search} no registrado en el padrón de contribuyentes. Detalles:\n{line}")

                    # Obtener Régimen Fiscal y Código Postal del RFC desde el archivo Excel
                    regimen_fiscal = excel_df.loc[excel_df["R.F.C."] == rfc_to_search, "Régimen Fiscal"].iloc[0]
                    codigo_postal = int(excel_df.loc[excel_df["R.F.C."] == rfc_to_search, "Código Postal"].iloc[0])

                    # Mostrar los datos en una tabla con color rojo
                    st.write("Detalles del RFC (No Válido):")
                    df_details = pd.DataFrame({"R.F.C.": [rfc_to_search], "Régimen Fiscal": [regimen_fiscal],
                                               "Código Postal": [codigo_postal], "Respuesta del SAT": [status_text]})
                    st.dataframe(df_details.style.applymap(color_cell_red, subset=["Respuesta del SAT"]))
                else:
                    st.warning(f"RFC {rfc_to_search} tiene un estado desconocido. Detalles:\n{line}")
                break
        else:
            st.warning(f"RFC {rfc_to_search} no encontrado en el archivo de texto.")
    else:
        st.error("Error al obtener el RFC desde el archivo Excel.")


# Función para aplicar colores a las celdas en función de la respuesta del SAT (color verde)
def color_cell(value):
    if "RFC válido" in value:
        return 'background-color: #8eff8e; color: black'  # Verde
    else:
        return ''  # Sin color

# Función para aplicar colores a las celdas en función de la respuesta del SAT (color rojo)
def color_cell_red(value):
    if "no registrado en el padrón de contribuyentes" in value:
        return 'background-color: #ff8e8e; color: black'  # Rojo
    else:
        return ''  # Sin color

def auxiliarPage(username):
    st.title(f"Panel de Auxiliar - Bienvenido, {username}")
    st.write("Acciones específicas para auxiliares")

    # Validar existencia de archivos en la carpeta "archivos"
    excel_files = [file for file in os.listdir("archivos") if file.endswith((".xls", ".xlsx"))]

    # Buscar específicamente el archivo "RESPUESTA_SAT_RFC.txt"
    txt_files = [file for file in os.listdir("archivos") if file == "RESPUESTA_SAT_RFC.txt"]

    if not excel_files or not txt_files:
        st.warning("No se encontraron los archivos necesarios. Contacte al administrador.")
    else:
        # Leer el archivo Excel
        if len(excel_files) > 1:
            selected_excel_file = st.selectbox("Seleccionar Archivo Excel", excel_files)
        else:
            selected_excel_file = excel_files[0]

        excel_df = pd.read_excel(os.path.join("archivos", selected_excel_file))

        # Seleccionar razón social desde el archivo Excel
        selected_reason_social = st.selectbox("Seleccionar Razón Social", excel_df["Razón Social"].tolist(),
                                              key="selectbox")

        # Botón para realizar la búsqueda
        if st.button("Comprobar estado de RFC"):
            # Buscar el RFC correspondiente en el archivo de texto
            txt_file_path = os.path.join("archivos", "RESPUESTA_SAT_RFC.txt")
            with open(txt_file_path, "r", encoding='latin-1') as txt_file:
                txt_content = txt_file.read()

            buscar_rfc_en_archivo_txt(excel_df, selected_reason_social, txt_content)

    # Botón para cerrar sesión
    if st.button("Cerrar Sesión"):
        st.session_state.username = None  # Asignar un valor nulo al nombre de usuario
        st.experimental_rerun()  # Recargar la aplicación para mostrar la página de inicio de sesión
