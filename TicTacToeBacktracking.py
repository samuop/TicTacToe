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

def play(board, player):
    if is_winner(board, 'X'):
        return -1
    elif is_winner(board, 'O'):
        return 1
    elif is_board_full(board):
        return 0
    
    best_score = float('-inf') if player == 'X' else float('inf')
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = player
                score = play(board, 'O' if player == 'X' else 'X')
                board[i][j] = ' '
                
                if player == 'X':
                    best_score = max(best_score, score)
                else:
                    best_score = min(best_score, score)
    
    return best_score

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
            
            best_score = float('-inf')
            best_move = None
            
            for i in range(3):
                for j in range(3):
                    if board[i][j] == ' ':
                        board[i][j] = 'O'
                        score = play(board, 'X')
                        board[i][j] = ' '
                        
                        if score > best_score:
                            best_score = score
                            best_move = (i, j)
            
            board[best_move[0]][best_move[1]] = 'O'
            
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
