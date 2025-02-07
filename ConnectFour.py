BOARD_SIZE = 7
ROW_SIZE = 6
WINNING_LENGTH = 4
p1 = 'X '
p2 = 'O '

slots = ['1', '2', '3', '4', '5', '6', '7']
board = [['* ' for x in range(BOARD_SIZE)] for y in range(ROW_SIZE)]

def print_board():
    print(" ".join(slots))
    for row in board:
        print("".join(row))

def set_player_character():
    global p1, p2
    change=input(("Player one you are X, would you like to change your character? Yes or No? "))
    if change.upper() == "YES":
        p1 = input("What character would you like to be? One letter only. ")
        if p1 == " " or len(p1) > 1:
            p1 = "X"
            print("Invalid character, you are X.")
    change=input(("Player two you are O, would you like to change your character? Yes or No? "))
    if change.upper() == "YES":
        p2 = input("What character would you like to be? One letter only. ")
        if p2 == " " or len(p1) > 1:
            p2 = "O"
            print("Invalid character, you are O.")
        if p1 == p2:
            p2 = "O"
            print("Invalid character, you are O.")

def open_row(column):
    for row in range(ROW_SIZE-1, -1, -1):
        if board[row][column] == '* ':
            return row
    return -1 # returns -1 if column is full

def check_horizontal(player, row, col):
    count = 0 # number of consecutive pieces
    for i in range(BOARD_SIZE): # loops through the row
        if board[row][i] == player: # checks if the piece is the same as the player
            count += 1 # increments count if piece is the same
            if count == WINNING_LENGTH: # if count = 4 that means player has won
                return True # returns True if player has won
        else:
            count = 0 #resets count if different piece is found
    return False 

def check_vertical(player, row, col):
    count = 0 # number of consecutive pieces
    for i in range(BOARD_SIZE): # loops through the column
        if board[i][col] == player: # checks if the piece is the same as the player
            count += 1
            if count == WINNING_LENGTH:
                return True
        else:
            count = 0 # resets count if different piece is found
    return False 

def check_diagonal(player, row, col):
    count = 0
    # checks \ diagonal
    # starts from (row, column) and goes down and to the right
    for i in range(BOARD_SIZE):
        if row + i < ROW_SIZE and col + i < BOARD_SIZE: 
            if board[row + i][col + i] == player: # checks if the piece is the same as the player
                count += 1 # add to count
                if count == WINNING_LENGTH:
                    return True
            else:
                count = 0
        else: 
            break
    #checks / diagonal
    #starts from (row, column) and goes up and to the right
    for i in range(WINNING_LENGTH):
        if row - i >= 0 and col + i < BOARD_SIZE:
            if board[row - i][col + i] == player: # checks if the piece is the same as the player
                count += 1 # add to count
                if count == WINNING_LENGTH:
                    return True
            else:
                count = 0
        else:
            break 
    return False

def check_win(player):
    for row in range(ROW_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == player:
                if check_horizontal(player, row, col) or check_vertical(player, row, col) or check_diagonal(player, row, col):
                    return True
    return False


def player_turn(player):
    if player == 1:
        current_player = p1
        print("Player one's turn.")
    else:
        current_player = p2
        print("Player two's turn.")
    column = int(input("Enter the column number you would like to place your piece. "))
    while column < 1 or column > 7:
        print("Invalid column number. Please enter a number between 1 and 7.")
        column = int(input("Enter the column number you would like to place your piece. "))
    while(open_row(column - 1) == -1):
        print(f"Column {column} is full.")
        column = int(input("Enter a different column number (1-7): "))
        while column < 1 or column > 7:
            print("Invalid column number. Please enter a number between 1 and 7.")
            column = int(input("Enter the column number you would like to place your piece (1-7): "))
        
    row = open_row(column - 1)
    board[row][column - 1] = current_player
    print_board()
    if check_win(current_player):
        print(f"Player {current_player} wins!")
        return True # ends game is theres winner
    else:
        return False 

def start_game():
    game_over = False
    print("Welcome to Connect Four!")
   # set_player_character()
    print_board()
    player = 1
    while not game_over:
        player_turn(player)
        player = 2 if player == 1 else 1
        if not any('* ' in row for row in board):
            print("It's a tie!")
            game_over = True
            break



start_game()
