# This program is an implementation of the game Tic Tac Toe (terminal-based, ASCII)
# Number of players is 2. Grid-size is customizable.

from art import *
import numpy as np


GRID_SIZE = 3


def main():
    
    print(text2art("Tic Tac Toe"))

    # Prompt users to start game, get player names
    n_matches = 0
    match = verify_game_start(n_matches)
    player_1, player_2 = get_players()

    print_custom_welcome(player_1, player_2)

    while match:
        # print starting-grid
        grid = reset()
        print_grid(grid)

        # Set number of turns and winner-boolean at start
        n_turns = GRID_SIZE * GRID_SIZE
        winner = False

        # Players take alternating turns until win / tie
        while n_turns > 0 and winner == False:
            if n_turns % 2 == 0:
                player = player_2
            else:
                player = player_1

            move = get_move(grid, player)
            update_grid(grid, move, player)
            print_grid(grid)
            winner = check_win(grid)

            if winner:
                print(text2art(f"{player['name']} wins!"))

            n_turns -= 1
        
        # Conditional tie statement
        if not winner:
            print(text2art("It's a tie!"))

        n_matches += 1

        # Check for rematch
        verify_game_start(n_matches)


# Prompt users to start game
def verify_game_start(n_matches):
    if n_matches == 0:
        answer = input('Do you want to play a game of Tic tac toe? y/n: ')
    else:
        answer = input('Do you want a rematch? y/n: ')

    if answer == 'n':
        print("\nOkay, goodbye! :)\n")
        exit()
    elif answer == 'y':
        return True
    else:
        print("\nInvalid answer. Please type y or n.\n")
        return verify_game_start(n_matches)


# Create player variables
def get_players():
    print("\nWhat are your names?\n")
    while True:
        player_1 = {'name': input("player 1: "), 'entry': 1}
        if not player_1['name'].strip():
            print("\nPlease enter a (nick)name\n")
        else:
            break

    while True:
        player_2 = {'name': input("player 2: "), 'entry': -1}
        if not player_2['name'].strip():
            print("\nPlease enter a (nick)name\n")
        else:
            break

    return player_1, player_2


# Print customised welcome text
def print_custom_welcome(player_1, player_2):
    print(f"\n\nWelcome {player_1['name']} and {player_2['name']}! \n")
    with open("welcome.txt", 'r') as f:
        print(f.read())


# Print the grid
def print_grid(grid):
    print("\n")
    dict = {0: ".", 1: "X", -1: "O"}
    for row in grid:
        for cell in row:
            print(f"{dict[cell]}   ", end = "")
        print("\n")


# Prompt user for a valid move
def get_move(grid, player):
    while True:
        try:
            n = int(input(f"{player['name']}, pick a position: "))

            if n in range(1,(GRID_SIZE * GRID_SIZE + 1)):
                row = int((n - 1) / GRID_SIZE)
                column = int(n % GRID_SIZE - 1)

                if grid[row][column] != 0:
                    print("\nNot a valid position. Please choose a position that is not occupied.\n")
                else:
                    return [row, column]
    
            else:
                print(f"\nNot a valid position. Please choose an integer between 1 and {GRID_SIZE ** 2}.\n")

        except ValueError:
            print("\nNot a valid position. Please enter an integer.\n")


# Update the grid with a move from a player
def update_grid(grid, move, player):
    grid[move[0]][move[1]] = player['entry']


# Check grid for win-conditions
def check_win(grid):
    row_sums = np.sum(grid, axis=0)
    column_sums = np.sum(grid, axis=1)
    diagonal_sum = np.trace(grid)
    reverse_diagonal_sum = np.trace(np.flipud(grid))

    # columns and rows
    for n in range(GRID_SIZE):
        if abs(row_sums[n]) == GRID_SIZE or abs(column_sums[n]) == GRID_SIZE:
            return True
    
    # diagonals
    if abs(diagonal_sum) == GRID_SIZE or abs(reverse_diagonal_sum) == GRID_SIZE:
        return True
        
    return False


# Returns a grid filled with zeros
def reset():
    return np.zeros((GRID_SIZE, GRID_SIZE))


if __name__ == "__main__":
    main()