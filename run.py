from random import randint

# Legend:
# " " available to guess
# X is hit on guess board
# O is miss

print("WELCOME TO OUR BATTLESHIP GAME!")


def get_name():
    """
    Ask for player's name, print thank you message\n
    Validate a string has been entered
    Returns:
    string (name)
    Prints:
    'not an appropriate name' if no name entered
    """
    name = ''
    while True:
        name = input("Please enter your name: ").capitalize()
        if name != '':
            print(f"Thank you for joining us {name}!")
            rules()
        else:
            print("This is not an appropriate name.")
            get_name()
        return name


def print_board(board):
    """
    The two boards are formatted with headers: \n
    Letters from A to H at the top of the 8 columns,\n
    numbers from 1 to 8 for the rows
    Arg:
    board: placeholder to format player_board to be printed\n
    and the computer_board, to be hidden
    """
    print("  A B C D E F G H")
    print("  -+-+-+-+-+-+-+-+")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1


def create_ships(board):
    """
    5 ships are placed at random by the computer \n
    by filling 5 empty cells with an X
    Arg:
    Int(5). Number of ships to be sunk

    """
    for ship in range(5):
        ship_row, ship_column = randint(0, 7), randint(0, 7)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = randint(0, 7), randint(0, 7)
        board[ship_row][ship_column] = "X"


def get_letters_to_numbers():
    """
    Dictionary, used in the get_ship_location
    to convert column letters to numbers
    Returns: string, 0 to 7
    """
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
    return letters_to_numbers


def get_ship_location():
    """
    The player enters coordinates to locate one ship at a time
    A valid number for row and letter for column are requested
    returns:
    row number - 1 (because column 1 is "0" for python)
    column letter (column string input converted to int)
    """
    letters_to_numbers = get_letters_to_numbers()
    row = input("Enter the row of the ship (1 to 8): ")
    while row not in "12345678":
        print("Not an appropriate choice, please enter a valid row")
        row = input("Enter the row of the ship (1 to 8): ")
    column = input("Enter the row of the ship (A to H): ").upper()
    while column not in "ABCDEFGH":
        print("Not an appropriate choice, please select a valid column")
        column = input("Enter the column of the ship (A to H): ").upper()
    return int(row) - 1, letters_to_numbers[column]


def count_hit_ships(board):
    """
    Counts how many ships have been sunk, screening for a X in the 64 cells
    Returns:
    count: an integer between 0 and 5
    """
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    print(f"Score = {count} out of 5")
    return count


def play_game():
    """
    Lists inside lists:
    Creates the two boards with 8 rows and columns
    Asks the player to enter a row and a column 10 times
    Prints:
    - player_board (strings), updated after each turn
    - results or error messages if invalid input (strings)
    - number of turns left (strings)
    - score (strings)
    """
    hidden_board = [[" "] * 8 for x in range(8)]
    guess_board = [[" "] * 8 for i in range(8)]
    create_ships(hidden_board)
    print_board(hidden_board)
    turns = 6
    while turns > 0:
        print('Guess a battleship location:')
        print_board(guess_board)
        row, column = get_ship_location()
        if guess_board[row][column] == "-":
            print("You guessed that one already")
        elif hidden_board[row][column] == "X":
            print("BATTLESHIP HIT!")
            guess_board[row][column] = "X"
            turns -= 1
        else:
            print("MISSED!")
            guess_board[row][column] = "O"
            turns -= 1
        if count_hit_ships(guess_board) == 5:
            print("You win!")
            quit()
        print(f"You have {turns} turn(s) left")
        if turns == 0:
            print("You've run out of turns: GAME OVER")
            break


def rules():
    """
    The player decides if he/she needs to read the rules
    The player then decide to continue or to quit the game
    Returns:
    strings: "y" or "n"
    """
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


def main():
    """
    Calls the main functions:
    get_name
    rules
    play_game functions from main()
    """
    get_name()
    rules()
    play_game()


main()