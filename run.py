from random import randint

# Legend:
# " " empty cell available to guess
# X for placing ship on the computer board and 'hit' ship on the player board
# - is miss

name = input("Please enter your name here: ")
print(f"Wecome to the game, {name.capitalize()}!")


def rules():
    c_rules = input("Do you know how to play? y/n: ").lower()
    if c_rules == "n":
        print(
            "You must destroy 5 ships placed at random by the computer "
            "on the grid. \nEach ship occupies one cell. \n"
            "Enter a number for a row and a letter for the column. \n"
            "You have 10 turns to destroy the computer's "
            "hidden fleet...\nGOOD LUCK!"
            )
        if input("Ready to play? y/n: ").lower() != "y":
            print("Sorry to see you leave...QUIT")
            quit()
    elif c_rules == "y":
        print("Ok, let's play then!")
        play_game()
    else:
        print("That is not a valid option. Please try again")
        rules()


def print_board(board):
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
        print("Not an appropriate choice, please enter a valid row")
        row = input("Enter the row of the ship (1 to 8): ")
    column = input("Enter the row of the ship (A to H): ").upper()
    while column not in "ABCDEFGH":
        print("Not an appropriate choice, please select a valid column")
        column = input("Enter the column of the ship (A to H): ").upper()
    return int(row) - 1, letters_to_numbers[column]

# To count the number of 'hits' the function counts the "X" across the 64 cells


def count_hit_ships(board):
    hits = 0
    for row in board:
        for column in row:
            if column == "X":
                hits += 1
    return hits


def play_game():
    """
    Prints the player-board
    """
    computer_board = [[" "] * 8 for x in range(8)]
    player_board = [[" "] * 8 for i in range(8)]
    create_ships(computer_board)
    turns = 10
    while turns > 0:
        print('Guess a battleship location:')
        print_board(player_board)
        row, column = get_ship_location()
        if player_board[row][column] == "-":
            print("You guessed that one already")
        elif player_board[row][column] == "X":
            print("It's a HIT!")
            player_board[row][column] = "X"
            turns -= 1
        else:
            print("You MISS!")
            player_board[row][column] = "O"
            turns -= 1
        if count_hit_ships(player_board) == 5:
            print("You win!")
            break
        print(f"You have {turns} turn(s) left")
        if turns == 0:
            print("You've run out of turns: GAME OVER")
            break


def main():
    rules()
    play_game()


main()
