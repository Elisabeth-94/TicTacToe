class Player:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.symbol = ""
        self.score = 0

    # Prompt user for a valid move
    def get_move(self, grid_size, play_field):
        while True:
            try:
                n = int(input(f"{self.name}, pick a position: "))

                if n in range(1,(grid_size * grid_size + 1)):
                    row = int((n - 1) / grid_size)
                    column = int(n % grid_size - 1)

                    if play_field.grid[row][column] != '.':
                        print("\nNot a valid position. Please choose a position that is not occupied.\n")
                    else:
                        return [row, column]
        
                else:
                    print(f"\nNot a valid position. Please choose an integer between 1 and {grid_size ** 2}.\n")

            except ValueError:
                print("\nNot a valid position. Please enter an integer.\n")