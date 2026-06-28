import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Análisis Exploratorio (EDA)", page_icon="📊", layout="wide")

st.title("📊 Análisis Exploratorio de Datos (EDA)")
st.markdown("En esta sección analizamos el comportamiento univariado, bivariado y multivariado de los usuarios.")

@st.cache_data
def load_data():
    return pd.read_csv('../data/processed/streaming_users_clean.csv')

try:
    df = load_data()
except Exception as e:
    st.error("No se pudo cargar el dataset.")
    st.stop()

# ==========================================
# 1. Univariado 1
# ==========================================
st.markdown("---")
st.subheader("1. Distribución de Edades (Univariado)")

fig1, ax1 = plt.subplots(figsize=(8, 4))
sns.histplot(df['age'], bins=20, kde=True, color='skyblue', ax=ax1)
ax1.set_title('Distribución de Edades de los Usuarios')
ax1.set_xlabel('Edad')
ax1.set_ylabel('Frecuencia')
st.pyplot(fig1)

st.info("**Interpretación:** La distribución es aproximadamente normal y centrada en adultos jóvenes (~33 años). Esto demuestra que el público objetivo principal de la plataforma está consolidado en el sector de mayor poder adquisitivo autónomo, aunque mantiene presencia en otros rangos.")

# ==========================================
# 2. Univariado 2
# ==========================================
st.markdown("---")
st.subheader("2. Adopción de Planes de Suscripción (Univariado)")

fig2, ax2 = plt.subplots(figsize=(8, 4))
sns.countplot(data=df, x='subscription_plan', order=['Básico', 'Estándar', 'Premium'], palette='viridis', ax=ax2)
ax2.set_title('Cantidad de Usuarios por Plan')
ax2.set_xlabel('Plan de Suscripción')
ax2.set_ylabel('Cantidad de Usuarios')
st.pyplot(fig2)

st.info("**Interpretación:** La plataforma sigue un modelo piramidal clásico. El plan Básico es el rey del mercado, reteniendo a casi la mitad de los usuarios. El salto al plan Premium representa la barrera comercial más dura.")

# ==========================================
# 3. Bivariado 1
# ==========================================
st.markdown("---")
st.subheader("3. Densidad de Consumo según el Plan (Bivariado)")

fig3, ax3 = plt.subplots(figsize=(8, 4))
sns.violinplot(data=df, x='subscription_plan', y='monthly_watch_time_mins', 
               order=['Básico', 'Estándar', 'Premium'], palette='Set2', inner='quartile', ax=ax3)
ax3.set_title('Densidad de consumo mensual por tipo de plan')
ax3.set_xlabel('Plan de Suscripción')
ax3.set_ylabel('Minutos por mes')
st.pyplot(fig3)

st.info("**Interpretación:** Los tres violines son virtualmente idénticos. Esto revela que pagar el plan más caro (Premium) no convierte al cliente en un usuario más activo. El enganche (engagement) con la plataforma es fuerte e independiente de lo que pagan.")

# ==========================================
# 4. Bivariado 2
# ==========================================
st.markdown("---")
st.subheader("4. Preferencia de Género por Plan (Bivariado)")

pivot = df.groupby(['subscription_plan', 'favorite_genre']).size().unstack(fill_value=0)
pivot_perc = pivot.div(pivot.sum(axis=1), axis=0) * 100
pivot_perc = pivot_perc.loc[['Básico', 'Estándar', 'Premium']]

fig4, ax4 = plt.subplots(figsize=(10, 5))
pivot_perc.plot(kind='bar', stacked=True, colormap='tab20', ax=ax4)
ax4.set_title('Proporción de géneros favoritos dentro de cada plan')
ax4.set_xlabel('Plan de Suscripción')
ax4.set_ylabel('Porcentaje (%)')
plt.legend(title='Género Favorito', bbox_to_anchor=(1.05, 1), loc='upper left')
st.pyplot(fig4)

st.info("**Interpretación:** Al igual que el tiempo de uso, los gustos de los usuarios son totalmente proporcionales en todos los planes. Las campañas de marketing de contenido (ej. estrenar una serie de Acción) tendrán el mismo impacto en usuarios de cualquier estrato de suscripción.")

# ==========================================
# 5. Multivariado
# ==========================================
st.markdown("---")
st.subheader("5. Matriz de Negocio: Usuarios por País y Plan (Multivariado)")

fig5, ax5 = plt.subplots(figsize=(10, 6))
pivot_heatmap = df.pivot_table(index='country', columns='subscription_plan', aggfunc='size')
pivot_heatmap = pivot_heatmap[['Básico', 'Estándar', 'Premium']]

sns.heatmap(pivot_heatmap, annot=True, fmt='d', cmap='YlGnBu', 
            linewidths=.5, ax=ax5, cbar_kws={'label': 'Cantidad de Usuarios'})
ax5.set_title('Distribución de Clientes por País y Plan')
ax5.set_xlabel('Plan de Suscripción')
ax5.set_ylabel('País')
st.pyplot(fig5)

st.info("**Interpretación:** El heatmap multivariado revela una constancia geográfica impresionante. Independientemente del país latinoamericano, la penetración de los tres planes mantiene exactamente las mismas proporciones. La empresa logró una estandarización de consumo transfronteriza.")
