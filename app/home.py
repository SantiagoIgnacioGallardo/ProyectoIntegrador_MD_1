import streamlit as st

st.set_page_config(
    page_title="Proyecto Integrador - Minería de Datos",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 Análisis de Usuarios de Streaming")
st.subheader("Proyecto Integrador — Minería de Datos I")

st.markdown("---")

st.markdown("""
### Contexto del Proyecto
En la era del contenido digital, comprender el comportamiento de los usuarios es vital para la retención y el crecimiento del negocio. 
Esta aplicación presenta un análisis profundo sobre los patrones de consumo de los clientes de una plataforma de streaming a nivel Latinoamérica.

A través de las distintas pestañas en la barra lateral, exploraremos desde la limpieza inicial de los datos, pasando por el **Análisis Exploratorio (EDA)**, 
hasta llegar a la reducción de dimensionalidad con **PCA** y nuestras **Conclusiones** finales sobre la fidelidad de los clientes según el plan que abonan.
""")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.info("""
    **Datos del Grupo**
    - **Integrantes:** Santiago Gallardo
    - **Tecnicatura:** Ciencia de Datos e IA
    - **Fecha de publicación:** Julio 2026
    """)

with col2:
    st.success("""
    **Repositorio Oficial**
    - https://github.com/SantiagoIgnacioGallardo/ProyectoIntegrador_MD_1
    """)
