from jogo_da_velha import verificaGanhador, token, branco


def movimentoIA(board, jogador):
    possibilidades = alternativas(board)
    melhor_movimento = None
    melhor_valor = None
    for possibilidade in possibilidades:
        board[possibilidade[0]][possibilidade[1]] = token[jogador]
        valor = miniMax(board, jogador)
        board[possibilidade[0]][possibilidade[1]] = branco

        if (melhor_valor is None):
            melhor_valor = valor
            melhor_movimento = possibilidade

        elif (jogador == 1):
            if (valor < melhor_valor):
                melhor_valor = valor
                melhor_movimento = possibilidade

    return melhor_movimento[0] , melhor_movimento[1]


def movimentoRobo(i,j):
    if i==0 and j == 0:
        return 1
    if i==0 and j==1:
        return 2
    if i ==0 and j==2:
        return 3
    
    if i==1 and j==0:
        return 4
    if i==1 and j==1:
        return 5
    if i==1 and j==2:
        return 6
    
    if i==2 and j==0:
        return 7
    if i==2 and j==1:
        return 8
    if i==2 and j==2:
        return 9
    


def alternativas(board):
    possibilidades = []

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                possibilidades.append([i, j])

    return possibilidades

score = {"EMPATE": 0,"X": 1,"O": -1}

def miniMax(board, jogador):
    ganhador = verificaGanhador(board)
    if(ganhador):
        return score[ganhador]
    
    jogador = (jogador + 1)%2
    
    possibilidades = alternativas(board)
    melhor_valor = None
    for possibilidade in possibilidades:
        board[possibilidade[0]][possibilidade[1]] = token[jogador]
        valor = miniMax(board, jogador)
        board[possibilidade[0]][possibilidade[1]] = branco

        if(melhor_valor is None):
            melhor_valor = valor
        elif(jogador == 0):
            if(valor > melhor_valor):
                melhor_valor = valor
        elif(jogador == 1):
            if(valor < melhor_valor):
                melhor_valor = valor

    return melhor_valor
