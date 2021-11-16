__author__ = None
__version__ = 0
__name__ = None


# Imports
...


class Game:  # Game class used to run the game
    def __init__(self):  # Define all thing that needs to be updated
        ...

    def update(self):  # Update all objects
        ...

    def run(self):  # Run the game
        while True:
            self.update()


print(f"{__name__}: {__version__}")
