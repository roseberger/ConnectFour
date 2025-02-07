BOARD_SIZE = 7
ROW_SIZE = 6
WINNING_LENGTH = 4
p1 = 'X'
p2 = 'O'

slots = ['1', '2', '3', '4', '5', '6', '7']
board = [[' ' for x in range(BOARD_SIZE)] for y in range(ROW_SIZE)]

def print_board():
    print("  ".join(slots))
    for row in board:
        print("* ".join(row))

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

def start_game():
    game_over = False
    print("Welcome to Connect Four!")
    set_player_character()
    print(p1, p2)
    #print_board()
    #player_turn()


start_game()
