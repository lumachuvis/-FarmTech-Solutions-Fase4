from machine import Pin, ADC, I2C
from time import sleep
import dht
import urandom
from lcd_api import LcdApi
from i2c_lcd import I2cLcd

# Configuração do I2C para o LCD
i2c = I2C(scl=Pin(22), sda=Pin(21), freq=400000)
lcd = I2cLcd(i2c, 0x27, 2, 16)  # Endereço I2C e configuração do LCD

# Configuração dos pinos
botao_P = Pin(12, Pin.IN, Pin.PULL_UP)
botao_K = Pin(13, Pin.IN, Pin.PULL_UP)
ldr = ADC(Pin(34))
ldr.atten(ADC.ATTN_11DB)
sensor_umidade = dht.DHT22(Pin(15))
rele = Pin(14, Pin.OUT)

# Função para ler os sensores
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

# Função de decisão de irrigação
def logica_irrigacao(nutriente_P, nutriente_K, nivel_ph, umidade_solo):
    if not nutriente_P or not nutriente_K or nivel_ph < 5.5 or umidade_solo < 40:
        rele.value(1)
        lcd.putstr("Irrigação: Ligada")
    else:
        rele.value(0)
        lcd.putstr("Irrigação: Desl.")

# Função para exibir os dados no LCD
def exibir_dados(nutriente_P, nutriente_K, nivel_ph, umidade_solo, temperatura):
    lcd.clear()
    lcd.putstr(f"P:{'Sim' if nutriente_P else 'Não'} K:{'Sim' if nutriente_K else 'Não'}\n")
    lcd.putstr(f"pH:{nivel_ph:.1f} Um:{umidade_solo:.1f}%\n")
    lcd.putstr(f"Temp:{temperatura}C")

# Loop principal
while True:
    nutriente_P, nutriente_K, nivel_ph, umidade_solo, temperatura = ler_sensores()

    # Exibir no monitor serial para depuração
    print(f"Nutriente P: {'Presente' if nutriente_P else 'Ausente'}")
    print(f"Nutriente K: {'Presente' if nutriente_K else 'Ausente'}")
    print(f"Nível de pH: {nivel_ph:.2f}")
    print(f"Umidade do Solo: {umidade_solo:.2f}%")
    print(f"Temperatura: {temperatura}C")

    # Exibir no LCD e gerenciar irrigação
    exibir_dados(nutriente_P, nutriente_K, nivel_ph, umidade_solo, temperatura)
    logica_irrigacao(nutriente_P, nutriente_K, nivel_ph, umidade_solo)

    sleep(5)
