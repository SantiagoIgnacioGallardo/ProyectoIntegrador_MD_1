import streamlit as st

st.set_page_config(page_title="Conclusiones y Próximos Pasos", page_icon="🎯", layout="wide")

st.title("🎯 Conclusiones del Proyecto")
st.markdown("---")

st.header("1. Hallazgos Centrales")
st.success("""
**La Homogeneidad como fortaleza del negocio.**  
A través de todo el análisis exploratorio y del modelo matemático PCA, hemos descubierto de forma consistente que el comportamiento de los clientes es uniforme en todos los estratos de la plataforma:
- Un usuario del Plan Básico invierte el mismo tiempo visualizando contenido que un usuario Premium (aprox. 12.6 horas mensuales).
- La preferencia de géneros (Acción, Comedia, Drama) es exactamente proporcional sin importar cuánto pague el usuario.
- A nivel geográfico en LATAM, las métricas comerciales y de soporte técnico mantienen el mismo comportamiento.

Esto nos indica que **el engagement con el producto es alto y no depende del poder adquisitivo o del plan contratado**.
""")

st.markdown("---")

st.header("2. Limitaciones del Análisis")
st.warning("""
El alcance de estas conclusiones se encuentra condicionado por la información disponible en el dataset:
- **Fotografía estática:** Contamos con datos estáticos sin dimensión temporal (series temporales), por lo que no podemos evaluar la evolución del consumo mes a mes o el abandono (Churn rate).
- **Falta de métricas operativas:** No contamos con información clave sobre el hardware utilizado (TV vs Celular), resolución de reproducción elegida o cantidad de perfiles creados por cuenta. Estas variables ausentes son probablemente los verdaderos motivadores para la contratación del plan Premium.
""")

st.markdown("---")

st.header("3. Próximos Pasos y Mejoras Futuras")
st.info("""
Para una próxima iteración analítica, se propone al equipo de Data Science:
1. **Integración de Telemetría:** Cruzar esta base de datos con los registros de uso de dispositivos y ancho de banda consumido para encontrar la verdadera diferencia de valor entre el plan Premium y el Básico.
2. **Modelo Predictivo de Churn:** Incorporar fechas de baja (cancelación) para predecir mediante Machine Learning qué usuarios homogéneos tienen mayor riesgo de abandonar la plataforma.
3. **Análisis NLP:** Aplicar Procesamiento de Lenguaje Natural a los textos de los tickets de soporte (en lugar de solo contarlos numéricamente) para categorizar las fallas del sistema.
""")
