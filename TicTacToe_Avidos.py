def is_winner(board, player):
    # Comprobación de las filas
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
    
    # Comprobación de las columnas
    for j in range(3):
        if all(board[i][j] == player for i in range(3)):
            return True
    
    # Comprobación de las diagonales
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    
    return False

def is_board_full(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return False
    return True

def print_board(board):
    for i in range(3):
        print("|", end="")
        for j in range(3):
            print(board[i][j], end="|")
        print()
        print("-------")

# Función principal
def tic_tac_toe():
    board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]
    
    print("¡Bienvenido al juego Tic Tac Toe!")
    
    while True:
        print_board(board)
        row = int(input("Ingrese la fila (0-2): "))
        col = int(input("Ingrese la columna (0-2): "))
        
        if board[row][col] == ' ':
            board[row][col] = 'X'
            
            if is_winner(board, 'X'):
                print_board(board)
                print("¡Has ganado!")
                break
            elif is_board_full(board):
                print_board(board)
                print("¡Empate!")
                break
            
            # Algoritmo ávido
            for i in range(3):
                for j in range(3):
                    if board[i][j] == ' ':
                        board[i][j] = 'O'
                        
                        if is_winner(board, 'O'):
                            print_board(board)
                            print("¡Has perdido!")
                            return
                        
                        board[i][j] = ' '
            
            # Si no hay ganador ni empate, seleccionamos una posición libre de manera aleatoria
            for i in range(3):
                for j in range(3):
                    if board[i][j] == ' ':
                        board[i][j] = 'O'
                        break
                if board[i][j] == 'O':
                    break
            
            if is_winner(board, 'O'):
                print_board(board)
                print("¡Has perdido!")
                break
            elif is_board_full(board):
                print_board(board)
                print("¡Empate!")
                break

# Ejecución del juego
tic_tac_toe()
