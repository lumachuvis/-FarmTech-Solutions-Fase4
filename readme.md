FIAP - Faculdade de Informática e Administração Paulista
<p align="center"> <a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Administração Paulista" border="0" width=40% height=40%></a> </p> <br>
Projeto de Irrigação Inteligente - FarmTech Solutions
Nome do grupo

FarmTech Solutions
👨‍🎓 Integrantes:

    <a href="https://www.linkedin.com/in/luma-x">Luma Santos de Oliveira</a>
    <a href="https://www.linkedin.com/company/inova-fusca">Celeste Santos</a>
    <a href="https://www.linkedin.com/company/inova-fusca">Wellington Nascimento</a>
 

👩‍🏫 Professores:
Tutor(a)

    <a href="https://www.linkedin.com/company/inova-fusca">Lucas Gomes Moreira</a>

Coordenador(a)

    <a href="https://www.linkedin.com/company/inova-fusca">André Godoi Chiovato</a>

📜 Descrição

Este projeto visa desenvolver um sistema de irrigação inteligente para gestão agrícola. Utilizando o microcontrolador ESP32, sensores de umidade, pH e nutrientes do solo (P e K), o sistema ajusta automaticamente a irrigação conforme as condições do solo.

O sistema armazena dados em um banco de dados MySQL, permitindo análise histórica e melhorias contínuas no gerenciamento agrícola. A lógica de irrigação baseia-se nos níveis de umidade, pH e presença de nutrientes, ativando a bomba d’água conforme necessário.

📁 Estrutura de pastas

    .github: Configurações específicas do GitHub.
    assets: Imagens e elementos não estruturados.
    config: Arquivos de configuração do projeto.
    document: Documentos do projeto e anexos complementares.
    scripts: Scripts auxiliares como deploy e backups.
    src: Código-fonte principal do projeto.
    README.md: Guia e documentação geral do projeto (este arquivo).

🔧 Como executar o código
Pré-requisitos:

    IDE: Thonny, VSCode ou IDE compatível com MicroPython.
    Microcontrolador: ESP32.
    Simulador: Wokwi (para simulações).
    Bibliotecas: dht, machine, time.

Instalação e Execução:

    Clone o repositório:

    git clone https://github.com/usuario/projeto-irrigacao.git
    cd projeto-irrigacao/src

    Configure o ambiente:
        Conecte o ESP32 à IDE.
        Carregue o arquivo principal para o ESP32.

    Execute a simulação no Wokwi.com se necessário.

🗃 Histórico de lançamentos

    0.5.0 - XX/XX/2024 - Ajuste na lógica de irrigação.
    0.4.0 - XX/XX/2024 - Implementação do banco de dados MySQL.
    0.3.0 - XX/XX/2024 - Adição de novos sensores.
    0.2.0 - XX/XX/2024 - Configuração inicial do projeto.
    0.1.0 - XX/XX/2024 - Configuração básica do ESP32.

📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
