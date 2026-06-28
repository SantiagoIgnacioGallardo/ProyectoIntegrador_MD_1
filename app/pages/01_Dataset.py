import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dataset y Limpieza", page_icon="🗂️", layout="wide")

st.title("🗂️ El Dataset")
st.markdown("---")

st.markdown("""
### 1. Descripción General
El dataset original (`streaming_users_dirty.json`) contenía **8160 registros** de usuarios de una plataforma de streaming, con atributos demográficos y de comportamiento.

### 2. Resumen de Calidad y Limpieza
Nuestro proceso ETL priorizó mantener la **realidad del negocio**, eliminando únicamente los valores físicamente imposibles:
* **Duplicados:** Se eliminaron 126 filas idénticas absolutas.
* **Outliers Imposibles:** Se apartaron edades negativas/superiores a 100 años, tickets negativos, y tiempos de visualización mayores a los minutos que posee un mes (44640 min).
* **Imputación:** Se utilizó la mediana para valores numéricos faltantes y se agrupó bajo la categoría "Otros" a los géneros sin especificar.
* **Parseo:** Se estandarizó el formato de fechas y se eliminaron registros con fechas completamente corruptas.
* **Retención Final:** Retuvimos a 7265 usuarios, manteniendo deliberadamente a los "Súper Usuarios" (Outliers estadísticos reales).
""")

st.markdown("---")
st.subheader("Vista Previa del Dataset Limpio")

@st.cache_data
def load_data():
    return pd.read_csv('../data/processed/streaming_users_clean.csv')

try:
    df = load_data()
    st.dataframe(df.head(50), use_container_width=True)
    st.caption(f"Mostrando 50 de {len(df)} registros totales.")
except Exception as e:
    st.error(f"Error al cargar los datos: Asegúrate de ejecutar la aplicación desde la carpeta raíz del proyecto. Detalle: {e}")
