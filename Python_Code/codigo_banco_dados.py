# Importação de bibliotecas
import pandas as pd
import numpy as np
import mysql.connector
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import streamlit as st

# Conexão com o banco de dados
conexao = mysql.connector.connect(
    host="localhost",
    user="root",  # Substitua pelo seu usuário
    password="sua_senha",  # Substitua pela sua senha
    database="FarmTech"
)
cursor = conexao.cursor()

# Consulta SQL para obter os dados
sql_query = "SELECT nutriente_P, nutriente_K, nivel_ph, umidade_solo, temperatura, irrigacao FROM dados_irrigacao"
df = pd.read_sql(sql_query, conexao)

# Preprocessamento de dados
X = df.drop("irrigacao", axis=1)
y = df["irrigacao"]

# Divisão dos dados
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Treinamento do modelo
modelo = RandomForestClassifier(random_state=42)
modelo.fit(X_train, y_train)

# Avaliação do modelo
predicoes = modelo.predict(X_test)
acuracia = accuracy_score(y_test, predicoes)

# Interface Streamlit
st.title("Sistema de Irrigação Inteligente")
st.subheader("Modelagem Preditiva usando Scikit-learn")

# Formulário interativo
st.sidebar.header("Insira os dados dos sensores:")
nutriente_P = st.sidebar.selectbox("Nutriente P (Presente/Ausente)", [1, 0])
nutriente_K = st.sidebar.selectbox("Nutriente K (Presente/Ausente)", [1, 0])
nivel_ph = st.sidebar.slider("Nível de pH", 0.0, 14.0, 7.0)
umidade_solo = st.sidebar.slider("Umidade do Solo (%)", 0.0, 100.0, 50.0)
temperatura = st.sidebar.slider("Temperatura (°C)", 15.0, 40.0, 25.0)

# Predição com entrada personalizada
dados_usuario = np.array([[nutriente_P, nutriente_K, nivel_ph, umidade_solo, temperatura]])
resultado = modelo.predict(dados_usuario)[0]
estado_irrigacao = "Ativada" if resultado else "Desativada"

# Exibição dos resultados
st.write(f"Acurácia do Modelo: {acuracia * 100:.2f}%")
st.write("### Previsão de Irrigação:")
st.write(f"Irrigação: **{estado_irrigacao}**")

# Relatório detalhado
st.write("### Relatório de Classificação:")
st.text(classification_report(y_test, predicoes))

# Fechar a conexão
cursor.close()
conexao.close()
