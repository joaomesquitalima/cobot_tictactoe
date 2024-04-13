# Jogo da Velha Robótico

Este projeto implementa um jogo da velha onde um robô colaborativo joga contra um jogador humano. O robô utiliza o protocolo Modbus TCP para se comunicar com um dispositivo físico que representa o tabuleiro do jogo. O jogador humano interage com o robô pressionando um botão físico para indicar sua jogada.

## Pré-requisitos

Certifique-se de ter as seguintes dependências instaladas:
- pyModbusTCP
- Python 3.x

Você pode instalar as dependências usando pip:

```
pip install pyModbusTCP
```

Antes de executar o script, certifique-se de configurar corretamente o endereço IP do servidor Modbus TCP, a porta e o ID do robô de destino. Você pode fazer isso modificando as seguintes variáveis no início do script:

```python
SERVER_IP = '192.168.1.254'
SERVER_PORT = 502
DEVICE_ID = 1
```


