import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

st.set_page_config(page_title="Reducción de Dimensionalidad (PCA)", page_icon="📉", layout="wide")

st.title("📉 Análisis de Componentes Principales (PCA)")
st.markdown("---")

@st.cache_data
def load_data():
    return pd.read_csv('../data/processed/streaming_users_clean.csv')

try:
    df = load_data()
except Exception as e:
    st.error("No se pudo cargar el dataset.")
    st.stop()

st.markdown("""
### 1. Variables Utilizadas y Escalamiento
El algoritmo PCA es exclusivamente numérico. Seleccionamos las tres variables cuantitativas del dataset:
`age`, `monthly_watch_time_mins`, y `customer_support_tickets`.

**Justificación del Escalamiento:**  
Debido a que `monthly_watch_time_mins` (valores de miles) dominaría matemáticamente a `customer_support_tickets` (valores de 0 a 20), aplicamos **StandardScaler** para igualar sus pesos.
""")

# Ejecución de PCA
features = ['age', 'monthly_watch_time_mins', 'customer_support_tickets']
X = df[features]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

pca = PCA()
X_pca = pca.fit_transform(X_scaled)
varianza_explicada = pca.explained_variance_ratio_
varianza_acumulada = np.cumsum(varianza_explicada)

# Gráficos
col1, col2 = st.columns(2)

with col1:
    st.subheader("Gráfico de Sedimentación")
    fig1, ax1 = plt.subplots(figsize=(6, 4))
    ax1.bar(range(1, len(varianza_explicada)+1), varianza_explicada, alpha=0.7, color='skyblue')
    ax1.step(range(1, len(varianza_acumulada)+1), varianza_acumulada, where='mid', color='red', marker='o')
    ax1.set_ylabel('Ratio de Varianza Explicada')
    ax1.set_xlabel('Componentes Principales')
    ax1.set_xticks([1, 2, 3])
    st.pyplot(fig1)
    
    st.info("**Interpretación:** No existe un 'codo' pronunciado. La varianza está distribuida casi uniformemente entre las 3 componentes (aprox. 33% cada una), demostrando que las variables originales son ortogonales (no correlacionadas).")

with col2:
    st.subheader("Proyección Biplot 2D")
    df['PC1'] = X_pca[:, 0]
    df['PC2'] = X_pca[:, 1]
    
    fig2, ax2 = plt.subplots(figsize=(6, 4))
    sns.scatterplot(data=df, x='PC1', y='PC2', hue='subscription_plan', palette='Set1', alpha=0.4, ax=ax2)
    ax2.set_xlabel(f'PC1 ({varianza_explicada[0]*100:.1f}%)')
    ax2.set_ylabel(f'PC2 ({varianza_explicada[1]*100:.1f}%)')
    st.pyplot(fig2)
    
    st.info("**Interpretación:** Al proyectar el comportamiento en 2D, vemos una nube estática donde los distintos planes (colores) están completamente superpuestos. No hay clústeres, reforzando la homogeneidad de la base de usuarios.")
