from machine import Pin, ADC
from time import sleep
import dht
import urandom  # Para gerar valores aleatórios

# Configuração dos pinos
botao_P = Pin(12, Pin.IN, Pin.PULL_UP)  # Nutriente P
botao_K = Pin(13, Pin.IN, Pin.PULL_UP)  # Nutriente K
ldr = ADC(Pin(34))                      # LDR para simular pH
ldr.atten(ADC.ATTN_11DB)                # Aumenta o range de leitura do LDR
sensor_umidade = dht.DHT22(Pin(15))     # Sensor de umidade DHT22
rele = Pin(14, Pin.OUT)                 # Relé para controle da bomba d'água

def ler_sensores():
    # Leitura dos botões para P e K (True se botão não pressionado, False se pressionado)
    nutriente_P = not botao_P.value()  # Botão pressionado indica presença de P
    nutriente_K = not botao_K.value()  # Botão pressionado indica presença de K

    # Leitura do LDR (representando o pH) com pequena variação aleatória
    nivel_ph = (ldr.read() * (14 / 4095)) + (urandom.getrandbits(4) - 8) * 0.1
    nivel_ph = max(0, min(14, nivel_ph))  # Garantir que o pH fique na escala de 0 a 14

    # Leitura de umidade com variação simulada
    sensor_umidade.measure()
    umidade_solo = sensor_umidade.humidity() + (urandom.getrandbits(4) - 8) * 0.1
    umidade_solo = max(0, min(100, umidade_solo))  # Garantir que a umidade fique na escala de 0 a 100

    temperatura = sensor_umidade.temperature()  # Temperatura permanece constante para simplificar

    return nutriente_P, nutriente_K, nivel_ph, umidade_solo, temperatura

def logica_irrigacao(nutriente_P, nutriente_K, nivel_ph, umidade_solo):
    # Lógica para acionar o sistema de irrigação
    if not nutriente_P or not nutriente_K or nivel_ph < 5.5 or umidade_solo < 40:
        rele.value(1)  # Liga o relé para irrigação
        print("Irrigação ativada")
    else:
        rele.value(0)  # Desliga o relé
        print("Irrigação desativada")

while True:
    # Lê os valores dos sensores
    nutriente_P, nutriente_K, nivel_ph, umidade_solo, temperatura = ler_sensores()

    # Exibe os valores lidos no monitor serial
    print("Nutriente P:", "Presente" if nutriente_P else "Ausente")
    print("Nutriente K:", "Presente" if nutriente_K else "Ausente")
    print("Nível de pH:", round(nivel_ph, 2))
    print("Umidade do Solo:", round(umidade_solo, 2))
    print("Temperatura:", temperatura)

    # Decide se liga ou desliga a irrigação
    logica_irrigacao(nutriente_P, nutriente_K, nivel_ph, umidade_solo)

    # Aguardar antes da próxima leitura
    sleep(5)
