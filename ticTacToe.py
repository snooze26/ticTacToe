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

    
player1Marker, player2Marker = playerInput()

# print(player1Marker)
# print(player2Marker)

        
        
        
