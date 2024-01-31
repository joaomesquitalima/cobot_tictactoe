from pyModbusTCP.client import ModbusClient
from pyModbusTCP import utils
from time import sleep
from jogo_da_velha import criarBoard,printBoard,getInputValido, enserirValor, verificaGanhador
from minimax import movimentoIA, movimentoRobo
SERVER_IP = '192.168.1.254'
SERVER_PORT = 502
DEVICE_ID = 1

print('tentando conectar')
client = ModbusClient(host=SERVER_IP, port=SERVER_PORT)

if client.open():
    print('Connetion to Robot %s:%d established sucesso' %(SERVER_IP,SERVER_PORT))

else:
    print('erro')
    exit()

play_pause = client.write_single_coil(7104,1)

sleep(1)
jogador = 0
board = criarBoard([2,2,2,2,2,2,2,2,2])

client.write_single_register(9000,0)

def analisar():
    lista = []
    while(len(lista) <=9):
        if sinal_verde:
            lista.append(1)
        elif sinal_vermelho:
            lista.append(0)
        elif sinal_laranja:
            lista.append(2)

    return lista

ganhador = None

while True:
    green_button = client.read_discrete_inputs(3,1)[0]
    red_button = client.read_discrete_inputs(4,1)[0]

    sinal_verde = client.read_coils(4,1)[0]
    sinal_vermelho = client.read_coils(5,1)[0]
    sinal_laranja = client.read_coils(6,1)[0]

    printBoard(board)
    if jogador == 0:
        print("Sua vez jogador")
        i = getInputValido("Insira a linha: ")
        j = getInputValido("Insira a coluna: ")
        r ,board = enserirValor(board,i,j,jogador)
    
    if jogador ==1:
        print("Sua vez computador")
        # lista = analisar()
        # board = criarBoard(lista)
        i,j = movimentoIA(board,jogador)
        r ,board = enserirValor(board,i,j,jogador)
        pos = movimentoRobo(i,j)
        client.write_single_register(9000,pos)
        

    if r:
        jogador = (jogador+1)%2

    ganhador = verificaGanhador(board)
    

    if ganhador:
        printBoard(board)
        break
    

if ganhador == "X":
    print("Voce ganhou")
    

if ganhador == "O":
    print("O computador venceu")
    client.write_single_register(9000,22)


    