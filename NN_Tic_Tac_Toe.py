#Tic Tac Toe Implementation
#Name: Nikhitha Nagalla
#UFID:66288276
"""                                                                  TIC-TAC-TOE GAME
This is a simple tic tac toe game which will played by 2 humans sharing the same keyboard.
This game is designed to start a new game, asks users for input, updates the game board,handles incorrect inputs,detects the winners as shown in the sample output.
"""

def printBoard(board):
    #Displays the game board.
    row_sep="-"*18
    print(f"{row_sep}\n|R\\C| 0 | 1 | 2 |\n{row_sep}")
    r_index=0
    for row in board:
        print(f"| {r_index} | {' | '.join(row)} |")
        print(row_sep)

def resetBoard():
    #Initializes and resets the game board.
    return [[' ' for j in range(3)] for i in range(3)]

def validateEntry(row,col,board):
  #Validates the input - Returns True if the user entered valid inputs and the position is empty.
  if 0<=row<3 and 0<=col<3:
    if board[row][col]==" ":
      return True
    else:
      print("That cell is already taken\nPlease make another selection")
  else:
    print("Invalid entry: try again\nRow & Column numbers must be either 0,1, or 2.")

def checkFull(board):
    #Returns True if the board is full, otherwise returns False.
    return all(cell != ' ' for row in board for cell in row)

def checkWin(board, turn):
    #Returns True when a player wins, otherwise returns False.
    # Check rows for a win
    for row in board:
        if all(s == turn for s in row):
            return True
    # check columns for a win
    for col in range(3):
        if all(board[row][col] == turn for row in range(3)):
            return True
    # Check diagonals for a win
    if all(board[i][i] == turn for i in range(3)) or all(board[i][2 - i] == turn for i in range(3)):
        return True
    return False

def checkEnd(board, turn):
    #Returns True if the game is over (either a win or a draw)
    if checkWin(board, turn):
        print(f"\n{turn} IS THE WINNER!!!")
        return True
    elif checkFull(board):
        print("\nDRAW! NOBODY WINS!")
        return True
    return False

def start_tictactoe():
  #Main funtion to start the game
  board=resetBoard()
  present_turn="X"
  game_end=False
  print("New Game: X goes first.")
  print()
  while not game_end:
    printBoard(board)
    valid_move=False
    while not valid_move:
      #handling incorrect inputs
      try:
        print(f"\n{present_turn}'s turn:")
        print(f"Where do you want your {present_turn} placed?\nPlease enter row number and column number separated by a comma.")
        row,col=map(int,input().split(","))
        print(f"You have entered row #{row}\n          and column #{col}")
        valid_move=validateEntry(row,col,board)
      except ValueError:
        print("Invalid entry: try again.\nPlease enter row and column numbers as integers separated by a comma.")
    print("Thank you for your selection.")
    board[row][col]=present_turn

    game_end=checkEnd(board,present_turn)
    present_turn="O" if present_turn=="X" else "X" #swtiching the turns

    if game_end:
      printBoard(board)
      #Repeat the game
      replay=input("\nAnother game? Enter Y or y for yes.\n").strip().lower()
      if replay=="y":
        board=resetBoard()
        print("New Game: X goes first.")
        print()
        present_turn="X"
        game_end=False
      else:
        print("Thank you for playing!")

# Calling the main function to execute
start_tictactoe()
