from random import randint

# Legend:
# " " available to guess
# X is hit on guess board
# O is miss


# Dictionary, used in the get_ship_location
# to convert column letters to numbers
# Returns: string, 0 to 7
LETTERS_TO_NUMBERS = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7
}


def get_name():
    """
    Ask for player's name, print thank you message
    Validate a string has been entered
    Returns:
    string (name)
    Prints:
    'not an appropriate name' if no name entered
    """
    name = ''
    while True:
        name = input("  Please enter your name: ").strip().capitalize()
        if name != '':
            print(f"\n  Thank you for joining us {name}!")
            rules()
            break
        else:
            print("  This is not an appropriate name.")


def print_board(board):
    """
    The two boards are formatted with headers:
    Letters from A to H at the top of the 8 columns,
    numbers from 1 to 8 for the rows
    Arg:
    board: placeholder to format player_board to be printed
    and the computer_board, to be hidden
    """
    print("\n    A B C D E F G H")
    print("    -+-+-+-+-+-+-+-+")
    row_number = 1
    for row in board:
        print("  %d|%s|" % (row_number, "|".join(row)))
        row_number += 1


def create_ships(board):
    """
    20 ships are placed at random by the computer
    by filling 20 empty cells with an X
    Arg:
    Int(20). Number of ships to be sunk

    """
    for ship in range(20):
        ship_row, ship_column = randint(0, 7), randint(0, 7)
        while board[ship_row][ship_column] == "\033[31;1;1mX\033[0m":
            ship_row, ship_column = randint(0, 7), randint(0, 7)
        board[ship_row][ship_column] = "\033[31;1;1mX\033[0m"


def get_ship_location():
    """
    The player enters coordinates to locate one ship at a time
    A valid number for row and letter for column are requested
    returns:
    row number - 1 (because column 1 is "0" for python)
    column letter (column string input converted to int)
    """
    while True:
        try:
            row = input("\n  Enter the row of the ship (1 to 8): ").strip()
            if row in "12345678":
                row = int(row) - 1
                break
            else:
                print("\n  Wrong input, please select a row between 1 and 8")
        except ValueError:
            print("\n  Not an appropriate choice, please enter a valid row")
        except TypeError:
            print("\n  Not an appropriate choice, please enter a valid row")
    while True:
        try:
            column = input(
                "\n  Enter the column of the ship (A to H): ").strip().upper()
            if column in "ABCDEFGH":
                column = LETTERS_TO_NUMBERS[column]
                break
            else:
                print("\n  Wrong input, please select a column between A and H")
        except KeyError:
            print("\n  Not an appropriate choice, please select a valid column")
    return row, column


def count_hit_ships(board):
    """
    Counts how many ships have been sunk, screening for
    a X in the 64 cells
    Returns:
    count: an integer between 0 and 5
    Inside this function, the help_or_quit_game function is added
    to allow the player to quit the game after each go
    """
    help_or_quit_game()
    count = 0
    for row in board:
        for column in row:
            if column == "\033[31;1;1mX\033[0m":
                count += 1
    print(f"  Score = {count} out of 5")
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

    turns = 15
    while turns > 0:
        print(
            "  Guess a battleship location:\n"
            "  Legend: X is a hit; ~ is a miss"
        )
        print_board(guess_board)
        row, column = get_ship_location()
        if guess_board[row][column] == "\033[36;1;1m~\033[0m":
            print("\n  You guessed that one already\n")
        elif hidden_board[row][column] == "\033[31;1;1mX\033[0m":
            print("\n  BATTLESHIP SUNK!\n")
            guess_board[row][column] = "\033[31;1;1mX\033[0m"
            turns -= 1
        else:
            print("\n  YOU MISSED\n")
            guess_board[row][column] = "\033[36;1;1m~\033[0m"
            turns -= 1
        if count_hit_ships(guess_board) == 5:
            print("\n  YOU WIN!\n")
            print_board(guess_board)
            quit()
        print(f"  You have {turns} turn(s) left\n")
        if turns == 0:
            print("\n  You've run out of turns: GAME OVER")
            print("  This is the computer board:")
            print_board(hidden_board)
            if input(
                "\n  Type 's' to start again or any other key to quit: "
                    ).strip().lower() == "s":
                play_game()
            else:
                quit()


def rules():
    """
    The player decides if he/she needs to read the rules
    The player then decide to continue or to quit the game
    Returns:
    strings: "y" or "n"
    """
    c_rules = input("\n  Do you know how to play? y/n: ").strip().lower()
    if c_rules == "n":
        print(
            "\n  You must destroy 5 ships placed at random by the computer\n"
            "  on the board. Each ship occupies one cell.\n"
            "  Enter a number for a row and a letter for the column.\n"
            "  You have 15 turns to do serious damage to the computer's\n"
            "  hidden fleet...which counts 20 ships in total\n\n  GOOD LUCK!\n"
            )
        if input("  Ready to play? y/n: ").strip().lower() != "y":
            print("  Sorry to see you leave...QUIT")
            quit()
        else:
            play_game()
    elif c_rules == "y":
        print("\n  Ok, let's play then!")
        play_game()
    else:
        print("  That is not a valid option. Please try again")


def help_or_quit_game():
    """
    The player can decide to get some help by pressing "h"
    or quit at any time during the game by pressing 'q'
    """
    help_or_quit = input(
        "\n  Type any key to continue, 'h' for help \n"
        "  or 'q' to quit: ").strip().lower()
    if help_or_quit == "h":
        if help_or_quit == "h":
            print(
                "\n  -----------------------------------------\n"
                "  When you guess a row and a column\n"
                "  you either miss or hit a battleship:\n"
                "  A red X is a hit; a blue 'wave' is a miss\n"
                "  There are 20 hidden ships: you only need\n"
                "  to find 5 ships to win!\n"
                "  -----------------------------------------"
                )
    elif help_or_quit == "q":
        quit()
    else:
        pass


def main():
    """
    Calls the main functions:
    get_name
    rules
    play_game functions from main()
    """
    print("\n          \033[36;1;1mWELCOME TO THE BATTLESHIP GAME!\033[0m\n\n")
    get_name()
    rules()
    play_game()


main()
