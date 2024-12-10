# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="Images/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# FarmTech Solutions - Fase 4

## Grupo 10

## 👨‍🎓 Integrantes: 

- <a href="https://www.linkedin.com/in/luma-x">Luma Santos de Oliveira</a>
- <a href="https://www.linkedin.com/company/inova-fusca">Celeste Santos</a>
- <a href="https://www.linkedin.com/company/inova-fusca">Wellington Nascimento</a>
 

## 👩‍🏫 Professores:
### Tutor(a)
- <a href="https://www.linkedin.com/company/inova-fusca">Lucas Gomes Moreira</a>

### Coordenador(a)

- <a href="https://www.linkedin.com/company/inova-fusca">André Godoi Chiovato</a>

## 📋 Descrição do Projeto

O projeto FarmTech Solutions é uma solução integrada para monitoramento e controle inteligente de sistemas de irrigação agrícola. Ele combina um microcontrolador ESP32, sensores ambientais, um banco de dados relacional e uma interface web interativa para tomada de decisões com base em Machine Learning.

## 🚀 Melhorias Implementadas
🔧 Arquitetura de Software e Banco de Dados

    Banco de Dados Normalizado:
        Tabelas organizadas para melhor escalabilidade e desempenho.
        Registros categorizados em tabelas específicas:
            sensores: Cadastro de sensores instalados.
            registros_monitoramento: Leituras dos sensores ao longo do tempo.
            controle_irrigacao: Registro de ativações/desativações do sistema de irrigação.
            nutrientes_aplicados: Histórico de aplicação de nutrientes.
            logs_alertas: Registro de falhas e alertas críticos.

    Triggers e Procedimentos Armazenados:
        Automatização de cálculos de média e registros de alertas via procedimentos armazenados.

📡 Microcontrolador ESP32

    Gerenciamento de Sensores:
        Leitura contínua de sensores de umidade, pH e temperatura.
        Exibição dos dados em um display LCD conectado ao ESP32.

    Automação de Irrigação:
        Lógica de decisão melhorada para ativação/desativação automática do sistema de irrigação.

📊 Modelagem Preditiva e Interface Web

    Predição Inteligente:
        Modelo de aprendizado de máquina usando Scikit-learn.
        Predição em tempo real de necessidade de irrigação.

    Interface Interativa:
        Interface desenvolvida em Streamlit.
        Exibição gráfica de dados e previsões para o usuário final.

## 📚 Tecnologias Utilizadas
Tecnologia	Descrição
ESP32	Microcontrolador principal
Python	Back-end e análise de dados
MySQL	Banco de dados relacional
Streamlit	Interface web interativa
Scikit-learn	Modelagem preditiva
MicroPython	Programação do ESP32

## ⚙️ Como Configurar e Executar
1. Configuração do Banco de Dados

    Instale o MySQL Server.
    Execute o arquivo database_setup.sql para criar o banco de dados e suas tabelas.
    Configure suas credenciais de acesso ao banco no código-fonte.

2. Execução do ESP32

    Suba o código para o ESP32 usando a IDE Arduino ou similar.
    Conecte os sensores e o display LCD conforme o esquema elétrico fornecido.

3. Interface Web e Modelagem Preditiva

    Instale as dependências:

pip install -r requirements.txt

Execute a aplicação Streamlit:

streamlit run app.py


## 🗃 Histórico de lançamentos

    0.5.0 - XX/XX/2024 - Ajuste na lógica de irrigação.
    0.4.0 - XX/XX/2024 - Implementação do banco de dados MySQL.
    0.3.0 - XX/XX/2024 - Adição de novos sensores.
    0.2.0 - XX/XX/2024 - Configuração inicial do projeto.
    0.1.0 - XX/XX/2024 - Configuração básica do ESP32.

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
