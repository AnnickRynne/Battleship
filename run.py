from random import randint
# Legend:
# " " empty cell available to guess
# X for placing ship on the computer board and 'hit' ship on the player board
# - is miss

# THE BOARDS - 8 x 8 cells
# Computer board (hidden): used to contain 5 ships with random locations
COMPUTER_BOARD = [[" "] * 8 for x in range(8)]
# Player board (displayed):
# used to display the hit and miss targets after each turn
PLAYER_BOARD = [[" "] * 8 for x in range(8)]

# The top 3 lines print the columns heading, the for loop creates the grid
def print_board(board):
    print("  A B C D E F G H")
    print("  +-+-+-+-+-+-+-+")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1

# Python can only process numbers
letters_to_numbers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7
}

# Placing 5 ships at random by filling 5 empty cells with an X
def create_ships(board):
    for ship in range(5):
        ship_row, ship_column = randint(0, 7), randint(0, 7)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = randint(0, 7), randint(0, 7)
        board[ship_row][ship_column] = "X"

# The player is prompted to enter 2 coordinates to select a sinle cell.
# The data has to be valid

def get_ship_location():
    row = input("Enter the row of the ship (1 to 8): ")
    while row not in "12345678":
        print('Not an appropriate choice, please select a valid row')
        row = input("Enter the row of the ship: ")
    column = input("Enter the column of the ship (A to H): ").upper()
    while column not in "ABCDEFGH":
        print('Not an appropriate choice, please select a valid column')
        column = input("Enter the column of the ship: ")
    return int(row) - 1, letters_to_numbers[column]

# To count the number of 'hits' the function counts the "X" across the 64 cells
def count_hit_ships(board):
    hits = 0
    for row in board:
        for column in row:
            if column == "X":
                hits += 1
    return hits


create_ships(COMPUTER_BOARD)

# print_board(COMPUTER_BOARD)
# print_board(PLAYER_BOARD)

turns = 10
while turns > 0:
    print('Guess a battleship location:')
    print_board(PLAYER_BOARD)
    row, column = get_ship_location()
    if PLAYER_BOARD[row][column] == "-":
        print("You guessed that one already.")
    elif PLAYER_BOARD[row][column] == "X":
        print("It's a HIT!")
        PLAYER_BOARD[row][column] = "X"
        turns -= 1
    else:
        print("You MISS!")
        PLAYER_BOARD[row][column] = "O"
        turns -= 1
    if count_hit_ships(PLAYER_BOARD) == 5:
        print("You win!")
        break
    print(f"You have {turns} turns left")
    if turns == 0:
        print("You ran out of turns: GAME OVER")
        break
