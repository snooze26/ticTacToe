gameBoard = [" "]*10

def displayBoard(board):
    
    print(gameBoard[7] + "|" + gameBoard[8] + "|" + gameBoard[9])
    print(gameBoard[4] + "|" + gameBoard[5] + "|" + gameBoard[6])
    print(gameBoard[1] + "|" + gameBoard[2] + "|" + gameBoard[3])
    

def playerInput():
    acceptableValues = ["X", "O"]
    
    marker = ""
    
    while marker not in acceptableValues:
        marker = input("Player 1 turn, choose X or O: ")

    player1 = marker
    
    if player1 == "X":
        player2 = "O"
    else:
        player2 = "X"
    
    return (player1, player2)

def boardPosition(board, marker, position):
    board[position] = marker



def winner(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or ##top row
     (board[4] == mark and board[5] == mark and board[6] == mark) or # middle row
     (board[1] == mark and board[2] == mark and board[3] == mark) or # bottom row
     (board[1] == mark and board[5] == mark and board[9] == mark) or #diag bottom left to top right
     (board[3] == mark and board[5] == mark and board[7] == mark) or #diag bottom right to top left
     (board[3] == mark and board[6] == mark and board[9] == mark) or #down the right side
     (board[1] == mark and board[4] == mark and board[7] == mark) or #down the left side
     (board[2] == mark and board[5] == mark and board[8] == mark) #down the middle
    )

boardPosition(gameBoard, "X", 8)
boardPosition(gameBoard, "X", 5)
boardPosition(gameBoard, "X", 2)

displayBoard(gameBoard)
print(winner(gameBoard, "X"))
            
        
        
