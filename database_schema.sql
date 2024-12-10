-- Criação do banco de dados
CREATE DATABASE IF NOT EXISTS FarmTech;

USE FarmTech;

-- Tabela principal: Sensores
CREATE TABLE sensores (
    sensor_id INT AUTO_INCREMENT PRIMARY KEY,
    tipo_sensor VARCHAR(50) NOT NULL, 
    localizacao VARCHAR(100),          
    descricao TEXT,                   
    data_instalacao DATE
);

-- Tabela de Registros de Monitoramento
CREATE TABLE registros_monitoramento (
    registro_id INT AUTO_INCREMENT PRIMARY KEY,
    sensor_id INT,
    valor FLOAT NOT NULL,             
    unidade_medida VARCHAR(20),       
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (sensor_id) REFERENCES sensores(sensor_id) ON DELETE CASCADE
);

-- Tabela de Controle de Irrigação
CREATE TABLE controle_irrigacao (
    irrigacao_id INT AUTO_INCREMENT PRIMARY KEY,
    status BOOLEAN NOT NULL,           
    nivel_ph FLOAT,                  
    umidade_min FLOAT,                
    temperatura_max FLOAT,           
    motivo TEXT,                       
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabela de Nutrientes Aplicados
CREATE TABLE nutrientes_aplicados (
    aplicacao_id INT AUTO_INCREMENT PRIMARY KEY,
    tipo_nutriente VARCHAR(50) NOT NULL, 
    quantidade FLOAT,                     
    unidade_medida VARCHAR(20),           
    data_aplicacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabela de Logs de Alertas e Eventos
CREATE TABLE logs_alertas (
    alerta_id INT AUTO_INCREMENT PRIMARY KEY,
    tipo_alerta VARCHAR(100),              
    descricao TEXT,                       
    nivel_importancia INT,               
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
