BOARD_SIZE = 7
ROW_SIZE = 6
WINNING_LENGTH = 4

slots = ['1', '2', '3', '4', '5', '6', '7']
board = [[' ' for x in range(BOARD_SIZE)] for y in range(ROW_SIZE)]

def print_board():
    print("  ".join(slots))
    for row in board:
        print("* ".join(row))

def start_game():
    print("Welcome to Connect Four!")
    
    #print_board()
    #player_turn()


start_game()
