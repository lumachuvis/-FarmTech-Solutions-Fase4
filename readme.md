# Projeto de Irrigação Inteligente - FarmTech Solutions

## Descrição do Projeto

Este projeto foi desenvolvido como parte do sistema de gestão agrícola da *FarmTech Solutions*. O objetivo é criar um sistema de irrigação automatizado e inteligente que monitore a umidade do solo, os níveis de nutrientes (P e K) e o pH do solo, ajustando automaticamente a irrigação com base nas condições do solo.

O sistema utiliza o ESP32 para monitorar sensores e controlar um relé que representa a bomba d'água. Os dados dos sensores são armazenados em um banco de dados MySQL, permitindo uma análise histórica das condições do solo e do estado da irrigação.

## Componentes e Simulação no Wokwi

Como o Wokwi não possui sensores específicos para agricultura, usamos os seguintes componentes para representar os sensores necessários:

- *Botões*: Representam os sensores de nutrientes P e K. Um botão pressionado indica a presença do nutriente, enquanto um botão não pressionado indica ausência.
- *LDR (Light Dependent Resistor)*: Representa o sensor de pH. Valores analógicos do LDR simulam a variação de pH do solo (de 0 a 14).
- *DHT22*: Sensor de umidade do solo e temperatura.
- *Relé*: Representa a bomba d'água que liga/desliga conforme a necessidade de irrigação.

## Lógica de Controle da Irrigação

A lógica para ligar/desligar a irrigação é baseada nos seguintes critérios:
- *Nutrientes*: Se um dos nutrientes (P ou K) estiver ausente (botão não pressionado), a irrigação é ativada.
- *pH*: Se o nível de pH for inferior a 5.5, o sistema considera o solo ácido e ativa a irrigação para balancear.
- *Umidade do Solo*: Se a umidade do solo estiver abaixo de 40%, a irrigação é ativada.
- *Temperatura*: A temperatura é monitorada, mas não afeta a decisão de irrigação neste projeto.

Esses critérios podem ser ajustados conforme a necessidade agrícola específica.

## Configuração do Circuito no Wokwi

1. *Botão 1 (Nutriente P)*: Conectado ao pino GPIO 12 do ESP32.
2. *Botão 2 (Nutriente K)*: Conectado ao pino GPIO 13 do ESP32.
3. *LDR (pH)*: Conectado ao pino GPIO 34 (entrada analógica) do ESP32.
4. *DHT22 (Umidade e Temperatura)*: Conectado ao pino GPIO 15 do ESP32.
5. *Relé (Bomba de Água)*: Conectado ao pino GPIO 14 do ESP32.

O circuito completo está disponível no Wokwi.com e pode ser simulado com os componentes acima.

## Código do ESP32 em MicroPython

O código abaixo é usado no ESP32 para monitorar os sensores e controlar o relé. Ele lê os valores dos sensores e decide quando ligar ou desligar a irrigação. 

```python
from machine import Pin, ADC
from time import sleep
import dht
import urandom  # Para gerar valores aleatórios

# Configuração dos pinos
botao_P = Pin(12, Pin.IN, Pin.PULL_UP)
botao_K = Pin(13, Pin.IN, Pin.PULL_UP)
ldr = ADC(Pin(34))
ldr.atten(ADC.ATTN_11DB)
sensor_umidade = dht.DHT22(Pin(15))
rele = Pin(14, Pin.OUT)

def ler_sensores():
    nutriente_P = not botao_P.value()
    nutriente_K = not botao_K.value()
    nivel_ph = (ldr.read() * (14 / 4095)) + (urandom.getrandbits(4) - 8) * 0.1
    nivel_ph = max(0, min(14, nivel_ph))
    sensor_umidade.measure()
    umidade_solo = sensor_umidade.humidity() + (urandom.getrandbits(4) - 8) * 0.1
    umidade_solo = max(0, min(100, umidade_solo))
    temperatura = sensor_umidade.temperature()
    return nutriente_P, nutriente_K, nivel_ph, umidade_solo, temperatura

def logica_irrigacao(nutriente_P, nutriente_K, nivel_ph, umidade_solo):
    if not nutriente_P or not nutriente_K or nivel_ph < 5.5 or umidade_solo < 40:
        rele.value(1)
        print("Irrigação ativada")
    else:
        rele.value(0)
        print("Irrigação desativada")

while True:
    nutriente_P, nutriente_K, nivel_ph, umidade_solo, temperatura = ler_sensores()
    print("Nutriente P:", "Presente" if nutriente_P else "Ausente")
    print("Nutriente K:", "Presente" if nutriente_K else "Ausente")
    print("Nível de pH:", round(nivel_ph, 2))
    print("Umidade do Solo:", round(umidade_solo, 2))
    print("Temperatura:", temperatura)
    logica_irrigacao(nutriente_P, nutriente_K, nivel_ph, umidade_solo)
    sleep(5)
