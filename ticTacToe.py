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

import random
def pickPlayer():
    if random.randint(0,1) == 0:
        return "Player 1"
    else: 
        return "Player 2"
    
def emptySpaceCheck(board, position):
    return board[position] == " "

def fullBoardCheck(board):
    for space in range(1,10):
        if emptySpaceCheck(board, space):
            return False
    return True

def playerChoice(board):
    acceptablevalues = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    boardPosition = 0

    while boardPosition not in acceptablevalues or not emptySpaceCheck(board, boardPosition):
        boardPosition = int(input("Choose your next position: (1-9) "))
    
    return boardPosition

def replay():
    bool = False
    choice = "wrong"
    
    while choice not in ["Y", "N"]:
        choice = input("Do you want to keep playing? ").upper()
        
        if choice not in ["Y", "N"]:
             print("Sorry, please choose Y or N")
        
    if choice == "Y":
        return True
    else:
        return False
    
def runGame():

    print("Welcome to Tic Tac Toe!")

    while True:
        gameBoardReset = [" "]*10            
        print(gameBoardReset)
        pickPlayer()


runGame()