CREATE DATABASE FarmTech;

USE FarmTech;

CREATE TABLE dados_irrigacao (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nutriente_P BOOLEAN,
    nutriente_K BOOLEAN,
    nivel_ph FLOAT,
    umidade_solo FLOAT,
    temperatura FLOAT,
    irrigacao BOOLEAN,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
