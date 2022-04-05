# Legend:
# " " available to guess
# X is hit on guess board
# - is miss

# THE BOARDS - 8 x 8 cells 
# Computer board (hidden): used to contain 5 ships with random locations
COMPUTER_BOARD = [[" "] * 8 for x in range(8)]
#Player board (displayed): used to display the hit and miss targets after each turn
PLAYER_BOARD = [[" "] * 8 for x in range(8)]

def print_board():
    print("  A B C D E F G H")
    print("  +-+-+-+-+-+-+-+")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1

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

def create_ships():
pass


def get_ship_coordinates():
pass


def count_hit_ships():
pass




