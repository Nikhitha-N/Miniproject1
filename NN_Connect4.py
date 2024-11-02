# Connect Four game implementation
#Name: Nikhitha Nagalla
#UFID:66288276
"""                                                                  CONNECT FOUR GAME 
This is a simple connect four game game which will played by 2 humans sharing the same keyboard.
This game is designed to start a new game, asks users for input, updates the game board,handles incorrect inputs,detects the winners as shown in the sample output.
"""


def printBoard(board):
    '''Print the board with a clean, formatted look '''
    for row in range(6, 0, -1):  # Start from row 6 down to 1
        print(f"| {row} ", end="")
        for col in range(7):
            print(f"| {board[row-1][col]} ", end="")
        print("|")
        print("-"*33)
    
    # Print the column labels
    print("|R/C| a | b | c | d | e | f | g |")
    print()

def resetBoard():
    '''Initializes and resets the game board.'''
    return [[' ' for i in range(7)] for j in range(6)]

def validateEntry(board, col, row):
    '''Validates the input - Returns True if the user entered valid inputs otherwise false. '''
    if col < 0 or col > 6 or row < 0 or row > 5:  # Check if the column and row indices are within bounds
        return False
    if board[row][col] != ' ': # Check if the selected cell is already taken
        return False
    if row > 0 and board[row-1][col] == ' ':         # Check if there is an empty cell directly above the selected cell
        return False
    return True

def checkFull(board):
    '''Returns True if the board is full, otherwise returns False.'''
    return all(board[5][col] != ' ' for col in range(7))

def availablePosition(board):
    """Return the list of available position to enable the users to make the valid moves"""
    positions = []
    for col in range(7):
        for row in range(6):
            if board[row][col] == ' ':
                positions.append(f"{chr(97+col)}{row+1}")  #Convert column index to letter and row index to number
                break
    return positions

def checkWin(board, turn):
    # Check horizontal
    for row in range(6):
        for col in range(4):
            if all(board[row][col+i] == turn for i in range(4)):
                return True
    
    # Check vertical
    for row in range(3):
        for col in range(7):
            if all(board[row+i][col] == turn for i in range(4)):
                return True
    
    # Check diagonal (bottom-left to top-right)
    for row in range(3):
        for col in range(4):
            if all(board[row+i][col+i] == turn for i in range(4)):
                return True
    
    # Check diagonal (top-left to bottom-right)
    for row in range(3, 6):
        for col in range(4):
            if all(board[row-i][col+i] == turn for i in range(4)):
                return True
    
    return False

def checkEnd(board, turn):
    '''Determines whether the game is completed or not'''
    return checkWin(board, turn) or checkFull(board)

def connect_4():
    """Main function for connect four game"""
    while True:
        board = resetBoard()
        turn = 'X'
        print("New game: X goes first.\n")
        
        while True:
            printBoard(board)
            print(f"\n{turn}'s turn.")
            print("Where do you want your", turn, "placed?")
            available = availablePosition(board)
            print(f"Available positions are: {available}")
            
            while True:
              move = input("\nPlease enter column-letter and row-number (e.g., a1): ")  # Taking move from user 
              col=ord(move[0])-ord('a') #convert column to index
              row=int(move[1])-1 #convert row to index
              if col>7 or row>6:  #if user selects any invalid move
                print(f"Invalid move. Try again from available moves\n{available}") 
              else:
                if validateEntry(board,col,row): #validates the user input
                  board[row][col]=turn   #assigning the turn ovver position
                  print(f"Thank you for your selection.")
                  break
                else:
                    print(f"The cells need to be selected from available moves only.\n{available}")

            
            if checkWin(board, turn):
                printBoard(board)
                print(f"{turn} IS THE WINNER!!!")
                break
            
            if checkFull(board):
                printBoard(board)
                print("It's a tie!")
                break
            
            turn = 'O' if turn == 'X' else 'X' #switching turns
        #Repeating the game
        repeat_game = input("Another game (y/n)? ")  
        if repeat_game.lower() != 'y':
            print("Thank you for playing!")
            break

#Calling main function to execute
connect_4()