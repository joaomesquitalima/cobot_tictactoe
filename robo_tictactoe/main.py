from pyModbusTCP.client import ModbusClient
from pyModbusTCP import utils
from time import sleep
from jogo_da_velha import criarBoard,printBoard,verificaGanhador
from minimax import movimentoIA, movimentoRobo
# from tocar import play_audio
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
jogador = 1

#inicia um board vazio
board = criarBoard([2,2,2,2,2,2,2,2,2])


ganhador = None
status = 0

client.write_single_register(9000,0)
client.write_single_register(9001,0)

turno = 0

while True:
    print('Aguardando botão...')
    while client.read_holding_registers(9002,1)[0] == 0:
        pass
        
    print(turno)
        
    # play_audio("minha_vez.mp3")
    # # # aguarda o fim da analise
        
    #recebe lista do robo
    lista_tm = client.read_holding_registers(9003, 18)
    
    print(lista_tm)
    lista = []

    #filtra a lista recebida do robo
    for i in range(len(lista_tm)):
        if i % 2 == 1:
            lista.append(lista_tm[i])
    #cria board apartir da lista
    print('Tabuleiro:', lista)
    board = criarBoard(lista)
    # printBoard(board)
    ganhador = verificaGanhador(board)

    # if ganhador:
    #     #altera status do jogo
    #     client.write_single_register(9002,pos)
        
    #devolve linha i e coluna j do board
    i,j = movimentoIA(board,jogador)

    #usa a linha e coluna pra devolver um numero que representa um ponto pro robo
    pos = movimentoRobo(i,j)
    
    # o robo recebe a variavel pos , onde irá ir pra um ponto no tabuleiro fisico
    client.write_single_register(9000,pos)

    # client.write_single_register(9002,0)


    sleep(1)
