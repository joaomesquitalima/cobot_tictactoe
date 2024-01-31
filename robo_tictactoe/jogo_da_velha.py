branco = " "
token = ["X","O"]


def criarBoard(lista):
    for i in range(len(lista)):
        if lista[i] == True:
            lista[i] = "X"
        elif lista[i] == False:
            lista[i] = "O"
        else:
            lista[i] = " "


    board = [
            [lista[0],lista[1],lista[2]],
            [lista[3],lista[4],lista[5]],
            [lista[6],lista[7],lista[8]]
        ]

    return board


def printBoard(board):
    for i in range(3):
        print("|".join(board[i]))
        if i <2:
            print('------')



def getInputValido(mensagem):

    try:
        n = int(input(mensagem))
        if n>3 or n<1:
            print("Erro")
            return getInputValido(mensagem)
        return n-1
        
            
    except:
        print("Insira uma entrada valida")
        getInputValido(mensagem)

   


def enserirValor(board,i,j,jogador):
    if board[i][j] == " ":
        board[i][j] = token[jogador]

    else:
        print("Lugar ocupado")
        return False , board
    
    return True ,board


def verificaGanhador(board):
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != " ":
            return board[i][0]
        
    for i in range(3):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != " ":
            return board[0][i]
        
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    
    if board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[2][0] != " ":
        return board[1][1]
    

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return False
            

    return "EMPATE"