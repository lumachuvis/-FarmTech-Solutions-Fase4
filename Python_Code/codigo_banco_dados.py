import mysql.connector
import random
import time
from datetime import datetime

# Conectar ao banco de dados MySQL
conexao = mysql.connector.connect(
    host="localhost",
    user="root",  # Substitua pelo seu usuário
    password="03071993Edu",  # Substitua pela sua senha
    database="FarmTech"  # Nome do banco de dados
)
cursor = conexao.cursor()


# Função para inserir dados no banco de dados
def inserir_dados(nutriente_P, nutriente_K, nivel_ph, umidade_solo, temperatura, irrigacao):
    sql = """
    INSERT INTO dados_irrigacao (nutriente_P, nutriente_K, nivel_ph, umidade_solo, temperatura, irrigacao)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    dados = (nutriente_P, nutriente_K, nivel_ph, umidade_solo, temperatura, irrigacao)
    cursor.execute(sql, dados)
    conexao.commit()
    print("Dados inseridos com sucesso:", dados)


# Função para gerar dados aleatórios simulados
def gerar_dados():
    # Nutrientes P e K simulados como booleanos (True = Presente, False = Ausente)
    nutriente_P = random.choice([True, False])
    nutriente_K = random.choice([True, False])

    # Nível de pH simulado com variação entre 0 e 14
    nivel_ph = round(random.uniform(0, 14), 2)

    # Umidade do solo com variação entre 0 e 100%
    umidade_solo = round(random.uniform(20, 80), 2)  # Ajuste conforme necessário

    # Temperatura simulada com variação entre 15 e 35 graus Celsius
    temperatura = round(random.uniform(15, 35), 1)

    # Lógica simples para ativar ou desativar a irrigação
    # Neste caso, a irrigação é ativada se a umidade estiver abaixo de 40% ou se pH for inferior a 5.5
    irrigacao = (umidade_solo < 40 or nivel_ph < 5.5)

    return nutriente_P, nutriente_K, nivel_ph, umidade_solo, temperatura, irrigacao


# Loop para inserir dados a cada intervalo
try:
    while True:
        # Gerar dados aleatórios
        dados_sensores = gerar_dados()

        # Inserir dados no banco de dados
        inserir_dados(*dados_sensores)

        # Aguardar 5 segundos antes da próxima inserção
        time.sleep(5)

except KeyboardInterrupt:
    print("Encerrando a gravação de dados.")

finally:
    # Fechar a conexão com o banco de dados
    cursor.close()
    conexao.close()