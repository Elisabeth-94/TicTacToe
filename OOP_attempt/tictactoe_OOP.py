# This program is an attempt at an object-oriented version of tic tac toe
# Grid size and number of players (1  to 8) is customizable, just for fun.

from art import *
from player import Player
from grid import Grid


GRID_SIZE = 3
N_PLAYERS = 2


def main():
    
    print(text2art("Tic Tac Toe"))

    # Prompt users to start game, get player names
    n_matches = 0
    match = verify_game_start(n_matches)
    players = get_players()

    print_custom_welcome(players)

    while match:
        # Print starting grid
        play_field = Grid(GRID_SIZE)
        play_field.draw()

        # Set number of turns and winner-boolean at start
        n_turns = GRID_SIZE * GRID_SIZE
        winner = False

        # Players take alternating turns until win / tie
        turn = 0
        while turn < n_turns and winner == False:
            player = players[turn % N_PLAYERS]
            move = player.get_move(GRID_SIZE, play_field)

            play_field.update(move, player.symbol)
            play_field.draw()
            winner = play_field.check_win(player.symbol)

            if winner:
                print(text2art(f"{player.name} wins!"))
                player.score += 1

            turn += 1
        
        # Conditional tie statement
        if not winner:
            print(text2art("It's a tie!"))

        # Print the scores
        print(f"The scores are:")
        for player in players:
            print(f"{player.name}: {player.score}")
        print("")
        
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
    players = []
    symbols = ['X', 'O', '!', '&', '#', '$', '@', '?']
    
    print(f"\nYou will be playing with {N_PLAYERS} players. What are your names?\n")
    for n in range(N_PLAYERS):
        while True:
            player = Player(input(f"Name player {n + 1}: "), n + 1)
            if not player.name.strip():
                print("\nPlease enter a (nick)name\n")
            else:
                while True:
                    symbols_str = " ".join(symbols)
                    player.symbol = input(f"Please choose one of the following symbols: [\033[1m {symbols_str} \033[0m]: ")
                    # \033[1m and \033[0m is code to print with bold letters
                    if player.symbol not in symbols:
                        print("Not a valid symbol.")
                    else:
                        break
                symbols.remove(player.symbol)
                players.append(player)
                print("")
                break
    return players


# Print customised welcome text
def print_custom_welcome(players):
    names = players[0].name
    for n in range (1, N_PLAYERS - 1):
        names += ", " + players[n].name
    names += " and " + players[N_PLAYERS - 1].name

    print(f"\n\nWelcome {names}! \n")
    with open("welcome.txt", 'r') as f:
        print(f.read())

    
if __name__ == "__main__":
    main()